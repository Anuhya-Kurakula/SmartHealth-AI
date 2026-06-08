def rag_response(question):

    return {
        "answer": (
            "RAG is temporarily disabled in deployment. "
            "Please use Groq-powered tools."
        ),
        "sources": ["Deployment Mode"]
    }