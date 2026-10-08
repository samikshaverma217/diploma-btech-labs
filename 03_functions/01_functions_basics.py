# Series 12 - Functions
# Numbers: 9,41,13,74,3,15,42,54,120,4,2

# 1. Simple Function
def greet():
    print("Hello from Labs!")

greet()

# 2. Function with Parameter - Table
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

print("\nTable 2:")
table(2)
print("\nTable 3:")
table(3)

# 3. Return - Add
def add(a, b):
    return a + b

print(f"\n42+54 = {add(42,54)}")
print(f"9+41 = {add(9,41)}")

# 4. SI - P=120,R=4,T=2
def si(p,r,t):
    return (p*r*t)/100

print(f"\nSI 120,4,2 = {si(120,4,2)}")

# 5. Even-Odd
def is_even(num):
    return num % 2 == 0

print(f"\n41 even? {is_even(41)}")
print(f"42 even? {is_even(42)}")

# 6. Largest
def largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

print(f"\nLargest 9,41,13 = {largest(9,41,13)}")

# 7. Default Param
def greet_student(name, college="Polytechnic"):
    print(f"Hello {name} from {college}")

greet_student("Samiksha")
greet_student("Khushi", "BTech")

# 8. *args - Sum all
def sum_all(*args):
    return sum(args)

print(f"\nSum 9,41,13,74,3,15 = {sum_all(9,41,13,74,3,15)}")

# 9. Lambda
square = lambda x: x**2
print(f"\nSquare 9 = {square(9)}")

# 10. Function calling function
def square_list(lst):
    return [square(n) for n in lst]

my_list = [9,41,13,74,3,15]
print(f"\nList: {my_list}")
print(f"Squared: {square_list(my_list)}")
