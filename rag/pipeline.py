from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from rag.generation.llm import (
    generate_answer,
    generate_general_answer
)

from rag.memory.conversation_memory import add_to_memory
from rag.memory.database_memory import save_chat
from rag.rewriting.query_rewriter import rewrite_query
from rag.reranking.reranker import rerank_documents


BASE_DIR = Path(__file__).resolve().parent.parent

FAISS_PATH = BASE_DIR / "vectorstore" / "faiss_index"


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={
        "local_files_only": True
    }
)


vectorstore = FAISS.load_local(
    str(FAISS_PATH),
    embeddings,
    allow_dangerous_deserialization=True
)


def ask_question(question):

    # Step 1: Query Rewriting
    question = rewrite_query(question)

    print("\nRewritten Question:", question)

    # Step 2: Retrieve documents
    docs_with_scores = vectorstore.similarity_search_with_score(
        question,
        k=5
    )

    # Step 3: Reranking
    docs_with_scores = rerank_documents(
        docs_with_scores
    )

    best_score = docs_with_scores[0][1]

    print("Best Score:", best_score)

    # Lower score = better match
    if best_score < 0.7:

        docs = [
            doc
            for doc, score in docs_with_scores
        ]

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        answer = generate_answer(
            context,
            question
        )

        if answer == "NOT_FOUND":

            print("PDF answer not found. Using Groq.")

            answer = generate_general_answer(
                question
            )

            sources = [
                "Groq General Knowledge"
            ]

        else:

            sources = list(
                set(
                    doc.metadata.get(
                        "source",
                        "Unknown"
                    )
                    for doc in docs
                )
            )

    else:

        print("No relevant PDF found. Using Groq.")

        answer = generate_general_answer(
            question
        )

        sources = [
            "Groq General Knowledge"
        ]

    # Step 4: Temporary Memory
    add_to_memory(
        question,
        answer
    )

    # Step 5: Persistent Database Memory
    save_chat(
        question,
        answer
    )

    return {
        "answer": answer,
        "sources": sources
    }