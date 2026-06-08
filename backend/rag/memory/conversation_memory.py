chat_history = []


def add_to_memory(question, answer):

    chat_history.append({
        "question": question,
        "answer": answer
    })

    # Keep only last 3 conversations
    if len(chat_history) > 3:
        chat_history.pop(0)


def get_memory():

    history = ""

    for chat in chat_history:
        history += f"""
User: {chat['question']}
Assistant: {chat['answer']}
"""

    return history