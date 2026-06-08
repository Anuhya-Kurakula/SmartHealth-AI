from agents.tools.calculator_tool import calculate_expression
from agents.tools.bmi_tool import calculate_bmi
from agents.tools.web_search_tool import search_web

from agents.rag_tool import rag_response

from agents.tools.health_tools import (
    symptom_checker,
    health_tips,
    prevention_tool,
    nutrition_tool,
    exercise_tool,
    water_intake,
    medicine_info
)


def route_tool(question):

    if not question:
        return {
            "answer": "Please enter a question.",
            "sources": []
        }

    q = question.lower()

    # BMI Tool
    if "bmi" in q:

        return {
            "answer": calculate_bmi(question),
            "sources": ["BMI Tool"]
        }

    # Calculator Tool
    elif any(op in q for op in [
        "+",
        "-",
        "*",
        "/",
        "calculate"
    ]):

        return {
            "answer": calculate_expression(question),
            "sources": ["Calculator Tool"]
        }

    # Medicine Tool
    elif any(word in q for word in [
        "medicine",
        "tablet",
        "drug",
        "uses of",
        "side effects of",
        "tell me about"
    ]):

        medicine_name = (
            q
            .replace("tell me about", "")
            .replace("uses of", "")
            .replace("side effects of", "")
            .replace("medicine", "")
            .replace("tablet", "")
            .replace("drug", "")
            .strip()
        )

        return {
            "answer": medicine_info(medicine_name)["answer"],
            "sources": ["Medicine Tool"]
        }

    # Symptom Checker
    elif any(word in q for word in [
        "fever",
        "headache",
        "cough",
        "cold",
        "vomiting",
        "pain"
    ]):

        return {
            "answer": symptom_checker(question)["answer"],
            "sources": ["Symptom Checker"]
        }

    # Health Tips
    elif "health tips" in q:

        return {
            "answer": health_tips()["answer"],
            "sources": ["Health Tips Tool"]
        }

    # Disease Prevention
    elif "prevent" in q:

        return {
            "answer": prevention_tool(question)["answer"],
            "sources": ["Disease Prevention Tool"]
        }

    # Nutrition Tool
    elif any(word in q for word in [
        "foods",
        "nutrition",
        "iron",
        "protein",
        "vitamin"
    ]):

        return {
            "answer": nutrition_tool(question)["answer"],
            "sources": ["Nutrition Tool"]
        }

    # Exercise Tool
    elif any(word in q for word in [
        "exercise",
        "workout",
        "weight loss",
        "belly fat"
    ]):

        return {
            "answer": exercise_tool(question)["answer"],
            "sources": ["Exercise Tool"]
        }

    # Water Intake Tool
    elif "water" in q:

        return {
            "answer": water_intake(question)["answer"],
            "sources": ["Water Intake Tool"]
        }

    # Web Search Tool
    elif any(word in q for word in [
        "latest",
        "current",
        "today",
        "news",
        "who is"
    ]):

        return {
            "answer": search_web(question),
            "sources": ["Web Search"]
        }

    # Default → RAG
    else:
        return {
              "answer": generate_general_answer(question),
        "sources": ["Groq LLM"]
    }