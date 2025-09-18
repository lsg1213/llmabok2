from typing import List
from google.adk.agents import Agent

from sentence_transformers import SentenceTransformer
model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")

from qdrant_client import QdrantClient
client = QdrantClient()

def get_best_sellers(query: str, limit: int = 3) -> List[dict]:
    """
        주어진 쿼리에 대해 벡터 유사도 검색을 통해 책을 찾아서 반환합니다.
       
        Args:
            query (str): 검색할 쿼리 문자열
            limit(int): 반환할 상위 k개의 책 수 (기본값: 3)

        Returns:
            List[dict]: 검색된 책의 리스트, 각 책은 딕셔너리 형태로 반환됩니다.
    """
    query_vector = model.encode(query).tolist()
    books = client.search(
        collection_name="bestsellers",
        query_vector=query_vector,
        limit=limit
    )
    return books
    # return [book.payload for book in books]

root_agent = Agent(
    name="book_agent",
    model="gemini-2.0-flash",
    instruction="사용자의 모든 질문에 **get_best_sellers** 도구를 사용하여 모든 후보군에 대해 조사하여 답하세요.",
    tools=[get_best_sellers]
)
