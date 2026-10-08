# Series 08 - Variables & Identifiers
# Rules + Examples + All operations

# 1. Valid Identifiers - Rules from Diploma Lab
# - Can have letters, digits, underscore
# - Cannot start with digit
# - Case-sensitive
# - Cannot be keyword

name = "Samiksha"
Name = "Khushi" # Different because case-sensitive
student_name = "Polytechnic Student" # snake_case - best practice
studentName = "Diploma" # camelCase - also valid
_student = "Private variable"
student1 = "Roll 54"
student2 = "Roll 42"

print(f"Variables: {name}, {Name}, {student_name}")
print(f"Roll numbers: {student1}, {student2}")

# 2. Invalid Identifiers (Don't use - will give error)
# 1student = "error" - cannot start with digit
# student-name = "error" - hyphen not allowed
# student name = "error" - space not allowed

# 3. Keywords - Cannot use as variable (33 keywords)
import keyword
print(f"\nPython Keywords: {keyword.kwlist}")
# ['False', 'None', 'True', 'and', 'as', 'assert', ...]

# 4. Variable Assignment - All ways
# Single assignment
x = 9
y = 41

# Multiple assignment
a, b, c = 9, 41, 13
print(f"\nMultiple: a={a}, b={b}, c={c}")

# Same value to multiple
p = q = r = 74
print(f"Same value: p={p}, q={q}, r={r}")

# Swapping - BTech interview question
m = 15
n = 3
print(f"\nBefore swap: m={m}, n={n}")
m, n = n, m
print(f"After swap: m={m}, n={n}")

# 5. Variable Types - Dynamic Typing
var = 9
print(f"\nvar={var}, type={type(var).__name__}")
var = "banana" # Same variable, different type now
print(f"var={var}, type={type(var).__name__}")
var = 3+4j
print(f"var={var}, type={type(var).__name__}")

# 6. Constants - By convention UPPER_CASE
PI = 3.14159
COLLEGE_NAME = "Polytechnic"
MAX_MARKS = 100

print(f"\nConstants: PI={PI}, COLLEGE={COLLEGE_NAME}")

# 7. From your lab - Using variables for calculations
# P=120, R=4, T=2, SI calculation
principal = 120
rate = 4
time = 2
simple_interest = (principal * rate * time) / 100
print(f"\nSI Calc: P={principal}, R={rate}, T={time} => SI={simple_interest}")

# 8. id() and type() - Memory address
num = 42
print(f"\nValue: {num}, ID: {id(num)}, Type: {type(num)}")

# 9. Deleting variable
temp = 100
print(f"temp={temp}")
del temp
# print(temp) # Now error - deleted
print("temp deleted")
