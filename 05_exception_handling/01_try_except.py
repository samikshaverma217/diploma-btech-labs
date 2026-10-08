# Series 14 - Exception Handling (try-except)
# Prevents program crash - Very Important for BTech

# 1. Basic try-except - ZeroDivision
print("1. Division:")
try:
    a = 42
    b = 0
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# 2. ValueError - Invalid input
print("\n2. Invalid Number:")
try:
    num = int("Samiksha") # error
    print(num)
except ValueError:
    print("Error: Please enter valid number")

# 3. Using your lab numbers
print("\n3. Your numbers:")
try:
    lst = [9,41,13,74,3,15]
    print(lst[10]) # index out of range
except IndexError:
    print("Error: Index out of range, list has only 6 elements")

# 4. Multiple except
print("\n4. Multiple except:")
try:
    num = int(input("Enter number (test): 41 "))
    # For GitHub demo, we use 41
    num = 41
    result = 100 / num
    print(f"100 / {num} = {result}")
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# 5. try-except-else
print("\n5. try-except-else:")
try:
    p, r, t = 120, 4, 2
    si = (p * r * t) / 100
except:
    print("Error in SI calculation")
else:
    print(f"SI calculated successfully: {si}")
    print("Else runs only if no error")

# 6. try-except-finally
print("\n6. try-finally (always runs):")
try:
    f = open("students.txt", "r")
    data = f.read()
    print(f"File read: {len(data)} chars")
except FileNotFoundError:
    print("File not found")
finally:
    print("Finally: Closing file (always runs)")
    try:
        f.close()
    except:
        pass

# 7. Custom error handling - Marks validation
print("\n7. Marks validation:")
def check_marks(marks):
    try:
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be 0-100")
        print(f"Marks {marks} is valid")
    except ValueError as e:
        print(f"Error: {e}")

check_marks(74)
check_marks(150)

# 8. Real lab example - Safe division
print("\n8. Safe division function:")
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid types"

print(f"42/6 = {safe_divide(42,6)}")
print(f"42/0 = {safe_divide(42,0)}")
print(f"42/'a' = {safe_divide(42,'a')}")
