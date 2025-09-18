import json
with open(r"C:\Users\usejen_id\Desktop\llmabok2\book_agent\best-seller-books.json", "r", encoding="utf-8") as f:
    books = json.load(f)

# pip install sentence-transformers hf_xet
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")

from qdrant_client.models import PointStruct, VectorParams, Distance
from qdrant_client import QdrantClient
points = [PointStruct(id=idx+1, vector=model.encode(book["description"]).tolist(),
                      payload=book) for idx, book in enumerate(books)]

client = QdrantClient(url="http://localhost:6333")
client.create_collection(
    collection_name="bestsellers",
    vectors_config=VectorParams(size=model.get_sentence_embedding_dimension(), distance=Distance.COSINE),
)
client.upsert(collection_name="bestsellers", points=points)
# result = client.query_points(
#     collection_name="bestsellers",
#     query=model.encode("역사와 인간의 관계").tolist(),
#     limit=3,
# )
