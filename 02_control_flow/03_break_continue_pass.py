# Series 11 - Break, Continue, Pass
# Important for loops - BTech interview questions

my_list = [9,41,13,74,3,15,42,54]

# 1. BREAK - Exit loop completely
print("1. BREAK - Stop when 74 found:")
for n in my_list:
    if n == 74:
        print(f"Found {n} - Breaking loop!")
        break
    print(f"Checking {n}")
print("Loop ended\n")

# 2. CONTINUE - Skip current iteration
print("2. CONTINUE - Skip 13:")
for n in my_list:
    if n == 13:
        print(f"Skipping {n}")
        continue
    print(f"Processing {n}")
print()

# 3. PASS - Do nothing, placeholder
print("3. PASS - Skip 41 but keep loop:")
for n in my_list:
    if n == 41:
        pass # TODO - will handle later
    else:
        print(f"Number: {n}")
print()

# 4. Break with While
print("4. While + Break - Find 15:")
i = 0
while i < len(my_list):
    if my_list[i] == 15:
        print(f"Found 15 at index {i}")
        break
    i += 1
print()

# 5. Continue - Print only even numbers from your lab
print("5. Even numbers only (using continue):")
for n in my_list:
    if n % 2!= 0: # odd
        continue
    print(f"{n} is even")

# 6. Pass - Empty function / class placeholder
print("\n6. PASS as placeholder:")

def my_future_function():
    pass # Will write later, no error

class MyFutureClass:
    pass

print("Pass used - no error even though empty")

# 7. Real use case - Search roll 54
print("\n7. Search Roll 54:")
rolls = [9,41,13,74,3,15,42,54,120]
search = 54
for roll in rolls:
    if roll!= search:
        continue
    print(f"Roll {search} found!")
    break
else:
    print("Not found") # else with for - runs if no break

# 8. All three in one
print("\n8. All three together:")
for i in range(1, 11):
    if i == 3:
        print(f"{i} - pass (do nothing)")
        pass
    elif i == 6:
        print(f"{i} - continue (skip)")
        continue
    elif i == 9:
        print(f"{i} - break (stop)")
        break
    print(f" -> Processing {i}")
