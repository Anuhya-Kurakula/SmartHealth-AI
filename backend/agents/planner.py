def decide_tool(question):

    question = question.lower()

    if "bmi" in question:
        return "bmi"

    elif "calculate" in question:
        return "calculator"

    elif "latest" in question:
        return "web"

    else:
        return "rag"