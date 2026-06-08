import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(context, question):

    prompt = f"""
You are SmartHealth AI.

Context:
{context}

Question:
{question}

Instructions:
1. Answer ONLY using the provided context.
2. Keep the answer clear and concise.
3. If the answer is not available in the context, return ONLY:

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

    answer = response.choices[0].message.content.strip()

    return answer


def generate_general_answer(question):

    memory = get_memory()

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
You are SmartHealth AI, a helpful healthcare assistant.

Rules:
- Answer health-related questions professionally.
- Use previous conversation context when needed.
- Keep answers concise and easy to understand.
- If the user asks non-health questions, answer normally.
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

    answer = response.choices[0].message.content.strip()

    return answer
