def rerank_documents(docs_with_scores):

    docs_with_scores.sort(
        key=lambda x: x[1]
    )

    return docs_with_scores[:3]