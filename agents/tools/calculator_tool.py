def calculate_expression(question):

    try:
        expression = (
            question.lower()
            .replace("calculate", "")
            .strip()
        )

        result = eval(expression)

        return str(result)

    except:

        return "Invalid expression"