# Series 10 - Loops (For + While)
# Tables 2,3,6 from your lab

# 1. FOR LOOP - Table of 2
print("Table of 2:")
for i in range(1, 11):
    print(f"2 x {i} = {2*i}")

# 2. Table of 3
print("\nTable of 3:")
for i in range(1, 11):
    print(f"3 x {i} = {3*i}")

# 3. Table of 6 - from your lab pattern
print("\nTable of 6:")
for i in range(1, 11):
    print(f"6 x {i} = {6*i}")

# 4. Table of any number - Using your numbers
num = 74
print(f"\nTable of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# 5. WHILE LOOP
print("\nWhile loop - 1 to 5:")
i = 1
while i <= 5:
    print(i)
    i += 1

# 6. While - Table of 9
print("\nWhile - Table of 9:")
i = 1
while i <= 10:
    print(f"9 x {i} = {9*i}")
    i += 1

# 7. Loop through list [9,41,13,74,3,15] from your lab
my_list = [9,41,13,74,3,15]
print(f"\nList: {my_list}")
for n in my_list:
    print(f"Number: {n}, Square: {n**2}")

# 8. Break & Continue
print("\nBreak at 41:")
for n in my_list:
    if n == 41:
        print("Found 41 - break")
        break
    print(n)

print("\nSkip 13 (continue):")
for n in my_list:
    if n == 13:
        continue
    print(n)

# 9. Nested Loop - Pattern
print("\nPattern:")
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

# 10. Sum using loop - Important
total = 0
for n in my_list:
    total += n
print(f"\nSum of {my_list} = {total}") # 155
