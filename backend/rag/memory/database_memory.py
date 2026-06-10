from chatbot.models import ChatHistory


def save_chat(question, answer):

    try:
        ChatHistory.objects.create(
            question=question,
            answer=answer
        )

    except Exception as e:
        print(f"Database save failed: {e}")


def get_recent_chats(limit=5):

    try:
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

    except Exception as e:
        print(f"Database read failed: {e}")
        return ""