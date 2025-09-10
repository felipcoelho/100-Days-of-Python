student_scores = [78, 65, 89, 90, 55, 47, 99, 82, 67, 73]

# total = sum(student_scores)
# print(f"Total score: {total}")
# print(f"Average score: {total / len(student_scores):.2f}")


# sum_scores = 0
# for score in student_scores:
#     sum_scores += score

# print(f"Total score (using loop): {sum_scores}")    
# highest_score = max(student_scores)
# print(f"Highest score: {highest_score}")

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"Highest score (using loop): {max_score}")