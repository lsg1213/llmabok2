import json
with open(r"C:\Users\usejen_id\Desktop\llmabok2\book_agent\best-seller-books.json", "r", encoding="utf-8") as f:
    books = json.load(f)

# pip install sentence-transformers hf_xet
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")

from qdrant_client.models import PointStruct, VectorParams, Distance, Filter
from qdrant_client import QdrantClient
points = [PointStruct(id=idx+1, vector=model.encode(book["description"]).tolist(),
                      payload=book) for idx, book in enumerate(books)]

client = QdrantClient(url="http://localhost:6333")
client.recreate_collection(
    collection_name="bestsellers",
    vectors_config=VectorParams(size=model.get_sentence_embedding_dimension(), distance=Distance.COSINE),
)
client.upsert(collection_name="bestsellers", points=points)
result = client.query_points(
    collection_name="bestsellers",
    query=model.encode("한강 작가의 소설이 아닌 작품 중에서 재미있는 거 알려줘").tolist(),
    query_filter=Filter(must_not=[{"key": "author", "match": {"value": "한강"}}]),
    limit=3,
)
breakpoint()
print(result.payloads)