import os
from groq import Groq
from rag.memory.conversation_memory import get_memory

client = Groq(
    api_key="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"
)


def rewrite_query(question):

    # Rewrite only follow-up questions
    rewrite_keywords = [
        "symptoms",
        "treatment",
        "prevention",
        "causes",
        "diagnosis",
        "how can it be prevented",
        "how is it treated"
    ]

    if question.lower().strip() not in rewrite_keywords:
        return question

    memory = get_memory()

    prompt = f"""
Previous Conversation:
{memory}

Current Question:
{question}

Use ONLY the latest topic from the conversation.

Examples:

What is dengue?
Symptoms?
→ What are the symptoms of dengue?

What is migraine?
How is it treated?
→ How is migraine treated?

Return ONLY the rewritten question.
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

    rewritten_question = (
        response.choices[0]
        .message.content
        .strip()
    )

    print("Rewritten Question:", rewritten_question)

    return rewritten_question
