import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from rag.pipeline import ask_question

question = "What are the symptoms of malaria?"

answer = ask_question(question)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)