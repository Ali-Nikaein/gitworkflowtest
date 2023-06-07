def calculate_average_grade(scores):
    total = sum(scores)
    average = total / len(scores)
    final_grade = ""
    if average >= 90:
        final_grade = "A"
    elif average >= 80:
        final_grade = "B"
    elif average >= 70:
        final_grade = "C"
    elif average >= 60:
        final_grade = "D"
    else:
        final_grade = "F"
    return final_grade
