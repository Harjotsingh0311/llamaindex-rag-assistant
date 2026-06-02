import streamlit as st
import chromadb

from llama_index.core import (
    VectorStoreIndex,
    Settings
)

from llama_index.vector_stores.chroma import ChromaVectorStore

from src.config import llm, embed_model

# -------------------------------
# Page Config
# -------------------------------

st.set_page_config(
    page_title="PDF RAG Assistant",
    page_icon="📄",
    layout="wide"
)

# -------------------------------
# Models
# -------------------------------

Settings.llm = llm
Settings.embed_model = embed_model

# -------------------------------
# Load Vector Store
# -------------------------------

@st.cache_resource
def load_index():

    client = chromadb.PersistentClient(
        path="vector_store"
    )

    collection = client.get_collection(
        "pdf_rag"
    )

    vector_store = ChromaVectorStore(
        chroma_collection=collection
    )

    index = VectorStoreIndex.from_vector_store(
        vector_store
    )

    return index

index = load_index()

query_engine = index.as_query_engine(
    similarity_top_k=5
)

# -------------------------------
# Sidebar
# -------------------------------

with st.sidebar:

    st.title("📄 PDF RAG")

    st.success("Vector DB Loaded")

    st.info("Model: Mistral")

    st.info("Embedding: BGE Small")

# -------------------------------
# Main Page
# -------------------------------

st.title("📄 PDF Research Assistant")

st.write(
    "Ask questions about your PDF document."
)

# -------------------------------
# Chat Memory
# -------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# -------------------------------
# User Input
# -------------------------------

prompt = st.chat_input(
    "Ask a question..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    response = query_engine.query(
        prompt
    )

    answer = str(response)

    with st.chat_message("assistant"):

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )