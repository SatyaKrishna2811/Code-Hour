grades_count = int(input().strip())
grades = [int(input().strip()) for i in range(grades_count)]

for grade in grades:
    if grade >= 38 and grade % 5 >= 3:
        grade += (5 - grade % 5)
    print(grade)

# or

# grades_count = int(input().strip())

# grades = []
# for _ in range(grades_count):
#     grades_item = int(input().strip())
#     grades.append(grades_item)

# rounded_grades = []
# for grade in grades:
#     if grade >= 38:
#         remainder = grade % 5
        
#         if remainder >= 3:
#             grade += (5 - remainder)
    
#     rounded_grades.append(grade)

# for final_grade in rounded_grades:
#     print(final_grade)