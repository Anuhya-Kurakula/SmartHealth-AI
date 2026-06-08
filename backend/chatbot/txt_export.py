def export_txt():

    chats = ChatHistory.objects.all()

    with open(
        "chat_history.txt",
        "w",
        encoding="utf-8"
    ) as file:

        for chat in chats:

            file.write(
                f"Question: {chat.question}\n"
            )

            file.write(
                f"Answer: {chat.answer}\n\n"
            )

    print("TXT file created")