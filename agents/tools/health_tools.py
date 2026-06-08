import os
import re
from groq import Groq


client = Groq(
    api_key="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"
)


# -----------------------------------
# Symptom Checker Tool
# -----------------------------------
def symptom_checker(question):

    prompt = f"""
A user reports:

{question}

Provide:

1. Possible conditions.
2. General advice.

Do not diagnose.
Advise consulting a healthcare professional.
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

    return {

        "answer":
        response.choices[0].message.content

    }


# -----------------------------------
# Health Tips Tool
# -----------------------------------
def health_tips():

    prompt = """
Provide 5 daily health tips.

Keep them simple.
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

    return {

        "answer":
        response.choices[0].message.content

    }


# -----------------------------------
# Disease Prevention Tool
# -----------------------------------
def prevention_tool(question):

    prompt = f"""
How can {question} be prevented?

Give bullet points.
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

    return {

        "answer":
        response.choices[0].message.content

    }


# -----------------------------------
# Nutrition Tool
# -----------------------------------
def nutrition_tool(question):

    prompt = f"""
Answer this nutrition question:

{question}

Provide food suggestions in bullet points.
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

    return {

        "answer":
        response.choices[0].message.content

    }


# -----------------------------------
# Exercise Recommendation Tool
# -----------------------------------
def exercise_tool(question):

    prompt = f"""
Recommend exercises for:

{question}

Use bullet points.
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

    return {

        "answer":
        response.choices[0].message.content

    }


# -----------------------------------
# Water Intake Calculator
# -----------------------------------
def water_intake(question):

    numbers = re.findall(r"\d+", question)

    if numbers:

        weight = float(numbers[0])

        water = round(weight * 0.035, 2)

        return {

            "answer":

            f"""
Recommended Water Intake:

{water} liters/day
            """

        }

    return {

        "answer":

        "Please provide your weight in kilograms."

    }


# -----------------------------------
# Medicine Tool
# -----------------------------------
def medicine_info(medicine_name):

    prompt = f"""
You are a healthcare information assistant.

Provide information about {medicine_name}.

Include:

1. Uses
2. Common side effects
3. General precautions

Keep the answer short and educational.

Do NOT prescribe dosage.
Do NOT replace professional medical advice.
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

    return {

        "answer":

        response.choices[0].message.content

    }