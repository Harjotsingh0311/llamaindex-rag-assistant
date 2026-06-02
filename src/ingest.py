import os
import fitz
import chromadb

from llama_index.core import (
    Document,
    VectorStoreIndex,
    Settings
)

from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.storage.storage_context import StorageContext

from config import llm, embed_model

Settings.llm = llm
Settings.embed_model = embed_model

DATA_FOLDER = "../data"

documents = []

print("\nLoading PDFs...\n")

for file in os.listdir(DATA_FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(DATA_FOLDER, file)

        print(f"Reading: {file}")

        pdf = fitz.open(pdf_path)

        text = ""

        for page in pdf:
            text += page.get_text()

        pdf.close()

        print(f"Characters extracted: {len(text)}")

        print("\nPreview:\n")
        print(text[:1000])
        print("\n" + "=" * 80 + "\n")

        documents.append(
            Document(
                text=text,
                metadata={"source": file}
            )
        )

client = chromadb.PersistentClient(
    path="../vector_store"
)

collection = client.get_or_create_collection(
    name="pdf_rag"
)

vector_store = ChromaVectorStore(
    chroma_collection=collection
)

storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)

print("Creating embeddings...\n")

index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context
)

print("\n✅ Vector Database Created Successfully!")