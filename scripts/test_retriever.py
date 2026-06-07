import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.load_local(
    "vectorstore/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

query = "What are the symptoms of dengue?"

results = vectorstore.similarity_search(query, k=3)

for i, doc in enumerate(results, start=1):
    print(f"\n===== Result {i} =====\n")
    print(doc.page_content[:1000])