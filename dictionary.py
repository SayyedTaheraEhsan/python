# Dictionary example
student = {
    "name": "Ali",
    "age": 20,
    "course": "Math",
    "marks": 85
}

# 1. keys()
print("Keys:", student.keys())

# 2. values()
print("Values:", student.values())

# 3. items()
print("Items:", student.items())

# 4. get()
print("Get age:", student.get("age"))

# 5. update()
student.update({"marks": 90})  # update marks
print("After update:", student)
