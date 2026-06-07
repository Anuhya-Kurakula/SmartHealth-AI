import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(context, question):

    prompt = f"""
Context:
{context}

Question:
{question}

Instructions:

1. Use ONLY the provided context.
2. If answer is unavailable in context return:

NOT_FOUND
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()


def generate_general_answer(question):

    memory = get_memory()

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
You are SmartHealth AI.

Rules:

- Answer health questions professionally.
- For non-health questions answer normally.
- Do NOT force medical context.
- If user asks names, politics, meanings, greetings, or casual questions, answer naturally.
- Recommend consulting a doctor only for medical questions.
"""
            },
            {
                "role": "user",
                "content": f"""
Previous Conversation:
{memory}

Question:
{question}
"""
            }
        ]
    )

    return response.choices[0].message.content.strip()