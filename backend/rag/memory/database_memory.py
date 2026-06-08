from chatbot.models import ChatHistory


def save_chat(question, answer):

    ChatHistory.objects.create(
        question=question,
        answer=answer
    )


def get_recent_chats(limit=5):

    chats = ChatHistory.objects.order_by(
        "-created_at"
    )[:limit]

    memory = ""

    for chat in reversed(chats):

        memory += (
            f"User: {chat.question}\n"
            f"Assistant: {chat.answer}\n\n"
        )

    return memory