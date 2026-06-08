from chatbot.models import ChatHistory
from reportlab.pdfgen import canvas


def export_pdf():

    chats = ChatHistory.objects.all()

    pdf = canvas.Canvas("chat_history.pdf")

    y = 800

    for chat in chats:

        pdf.drawString(
            50,
            y,
            f"Q: {chat.question}"
        )

        y -= 20

        pdf.drawString(
            50,
            y,
            f"A: {chat.answer}"
        )

        y -= 40

    pdf.save()

    print("PDF created successfully")


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

    print("TXT file created successfully")