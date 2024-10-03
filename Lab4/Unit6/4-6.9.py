grades = {'Alice': [85,90,92], 'Bob': [88,87,85], 'Charlie': [90, 91, 89]}
avearage_grades = {}

for student, grade_list in grades.items():
    avearage_grades[student] = sum(grade_list) / len(grade_list)
    
print("Average Grades:", avearage_grades)