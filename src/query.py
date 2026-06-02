import chromadb

from llama_index.core import (
    VectorStoreIndex,
    Settings
)

from llama_index.vector_stores.chroma import ChromaVectorStore

from config import llm, embed_model

Settings.llm = llm
Settings.embed_model = embed_model

client = chromadb.PersistentClient(
    path="../vector_store"
)

collection = client.get_collection(
    "pdf_rag"
)

vector_store = ChromaVectorStore(
    chroma_collection=collection
)

index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store
)

query_engine = index.as_query_engine(
    similarity_top_k=5,
    response_mode="tree_summarize"
)

print("\n🚀 PDF Chat Ready")
print("Type 'exit' to quit\n")

while True:

    question = input("Ask Question: ")

    if question.lower() == "exit":
        break

    response = query_engine.query(question)

    print("\nAnswer:\n")
    print(response.response)

    print("\n" + "=" * 70 + "\n")