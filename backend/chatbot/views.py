from django.http import JsonResponse
from rag.pipeline import ask_question


def chat(request):

    question = request.GET.get("question")

    result = ask_question(question)

    return JsonResponse({
        "question": question,
        "answer": result["answer"],
        "sources": result["sources"]
    })