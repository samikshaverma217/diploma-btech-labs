# Series 09 - Conditional Statements (If-Elif-Else)
# Numbers: 9,41,13,74,3,15,42,54,120,4,2

# 1. Simple If
marks = 74
if marks >= 40:
    print(f"Marks {marks}: PASS")

# 2. If-Else
marks = 13
if marks >= 40:
    print(f"Marks {marks}: PASS")
else:
    print(f"Marks {marks}: FAIL")

# 3. Grading System
marks = 74
if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "F"
print(f"Marks {marks}: Grade {grade}")

# 4. Nested If - SI from your lab P=120,R=4,T=2
p, r, t = 120, 4, 2
if p > 0:
    if r > 0:
        if t > 0:
            si = p * r * t / 100
            print(f"SI: P={p},R={r},T={t} => {si}")

# 5. Even-Odd
num = 41
if num % 2 == 0:
    print(f"{num} EVEN")
else:
    print(f"{num} ODD")

num = 42
if num % 2 == 0:
    print(f"{num} EVEN")

# 6. Largest of Three
a, b, c = 9, 41, 13
print(f"Numbers: {a},{b},{c}")
if a >= b and a >= c:
    print(f"Largest: {a}")
elif b >= a and b >= c:
    print(f"Largest: {b}")
else:
    print(f"Largest: {c}")

# 7. Ternary Operator
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age}: {status}")
