student_scores = [120, 123, 160, 301, 56, 70, 130]

#student_scores.sort()
#print(student_scores[-1])
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)