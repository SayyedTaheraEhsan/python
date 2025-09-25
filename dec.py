# Student Grades Dictionary
students = {"Ali": 85, "Sara": 92, "John": 78, "Mary": 88}
highest_student = max(students, key=students.get)
average_marks = sum(students.values()) / len(students)

print("Highest Marks:", highest_student, students[highest_student])
print("Class Average:", average_marks)

# Reverse Dictionary
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {}
for k, v in original.items():
    reversed_dict[v] = k
print("Reversed Dictionary:", reversed_dict)