from django.http import JsonResponse
from agents.agent_executor import execute_agent
from chatbot.models import ChatHistory


def chat(request):

    question = request.GET.get("question")

    result = execute_agent(question)

    return JsonResponse({
        "answer": result["answer"],
        "sources": result["sources"]
    })


def dashboard_stats(request):

    total_chats = ChatHistory.objects.count()

    recent_chats = list(
        ChatHistory.objects.order_by("-created_at")
        [:5]
        .values("question", "created_at")
    )

    return JsonResponse({
        "total_chats": total_chats,
        "recent_chats": recent_chats
    })