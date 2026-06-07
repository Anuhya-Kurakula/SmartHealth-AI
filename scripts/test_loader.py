import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from rag.ingestion.pdf_loader import load_pdfs

docs = load_pdfs()

print(f"\nTotal Pages Loaded: {len(docs)}")

print("\nFirst Page Preview:\n")

print(docs[0].page_content[:500])