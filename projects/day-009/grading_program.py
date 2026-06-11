student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}


for student, score in student_scores.items():
    if score >= 91:
        print(f"Outstanding")
    elif score >= 80:
        print(f"Exceeds Expectations")
    elif score >= 71:
        print(f"Acceptable")
    else:
        print(f"Fail")

student_grades[student] = grade