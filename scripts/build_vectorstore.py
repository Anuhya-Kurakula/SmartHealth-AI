import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from rag.ingestion.pdf_loader import load_pdfs
from rag.ingestion.chunker import chunk_documents

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

print("Loading PDFs...")
docs = load_pdfs()

print("Chunking...")
chunks = chunk_documents(docs)

print(f"Chunks: {len(chunks)}")

print("Generating Embeddings...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

vectorstore.save_local("vectorstore/faiss_index")

print("✅ FAISS Index Created Successfully")