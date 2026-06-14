def grade(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"

print(grade(75))
print(grade(50))
print(grade(30))
print(grade(12))
