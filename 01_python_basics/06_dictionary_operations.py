# Series 06 - Dictionary Operations (All Operations)
# Dictionary = Key:Value - Most used in Data Science

student = {
    "name": "Samiksha",
    "course": "Diploma CSE",
    "year": 2,
    "marks": [9, 41, 13, 74, 3, 15]
}
print(f"Dictionary: {student}")
print(f"Count: {len(student)}") # 4 keys

# 1. Accessing
print(f"\nName: {student['name']}")
print(f"Course: {student.get('course')}") # Safe way
print(f"Year: {student.get('year', 'Not Found')}")

# 2. Adding / Updating
student["college"] = "Polytechnic"
print(f"\nAfter adding college: {student}")

student["year"] = 3 # Update
print(f"After updating year: {student['year']}")

student.update({"branch": "CSE", "year": 3})
print(f"After update(): {student}")

# 3. Removing
removed = student.pop("college")
print(f"\nRemoved college: {removed}")
print(f"Dict now: {student}")

# popitem removes last inserted
last = student.popitem()
print(f"Popped last item: {last}")

student["college"] = "Polytechnic" # Add back
student["branch"] = "CSE"

# 4. Keys, Values, Items - Very Important
print(f"\nKeys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# 5. Loop through dictionary - BTech level
print("\n--- Looping ---")
for key, value in student.items():
    print(f"{key} : {value}")

# 6. Check membership - only checks keys
print(f"\nIs 'name' in dict? {'name' in student}") # True
print(f"Is 'Samiksha' in dict? {'Samiksha' in student}") # False - checks keys only
print(f"Is 'Samiksha' in values? {'Samiksha' in student.values()}") # True

# 7. Dictionary from your lab numbers - practical example
marks_dict = {
    "python": 74,
    "math": 41,
    "dbms": 13,
    "cn": 15
}
print(f"\nMarks Dict: {marks_dict}")
print(f"Max marks subject: {max(marks_dict, key=marks_dict.get)}") # python
print(f"Total marks: {sum(marks_dict.values())}") # 143
print(f"Average: {sum(marks_dict.values())/len(marks_dict):.2f}")

# 8. Clear
# marks_dict.clear()
