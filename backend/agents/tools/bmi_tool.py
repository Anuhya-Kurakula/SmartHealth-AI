import re


def calculate_bmi(question):

    try:

        numbers = re.findall(r"\d+\.?\d*", question)

        weight = float(numbers[0])
        height_cm = float(numbers[1])

        height_m = height_cm / 100

        bmi = weight / (height_m ** 2)

        return f"Your BMI is {round(bmi, 2)}"

    except:

        return "Unable to calculate BMI."