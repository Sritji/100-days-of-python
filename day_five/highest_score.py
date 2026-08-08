student_scores = [150, 129, 268, 368, 23, 173, 356, 345, 467, 475, 467, 465, 234, 756]

# total_exam_score = sum(student_scores)
# print(total_exam_score)

sum = 0
for score in student_scores:
    sum+= score
print(sum)    

max_exam_score = max(student_scores)
print(max_exam_score)

max_score = 0
for score in student_scores:
    if score > max_exam_score:
        max_score = score
print(max_score)  