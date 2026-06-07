import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from rag.ingestion.pdf_loader import load_pdfs
from rag.ingestion.chunker import chunk_documents

docs = load_pdfs()

chunks = chunk_documents(docs)

print(f"Total Documents : {len(docs)}")
print(f"Total Chunks    : {len(chunks)}")

print("\nSample Chunk:\n")
print(chunks[0].page_content[:500])