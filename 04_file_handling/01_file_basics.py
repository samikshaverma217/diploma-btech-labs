# Series 13 - File Handling
# Read, Write, Append - Important for Diploma Lab

# 1. WRITE - Create new file
f = open("students.txt", "w")
f.write("Roll 9,41,13,74,3,15,42,54\n")
f.write("P=120,R=4,T=2,SI=9.6\n")
f.write("Samiksha - Diploma BTech Labs\n")
f.close()
print("File written: students.txt")

# 2. READ - Read full file
f = open("students.txt", "r")
data = f.read()
print(f"\nReading file:\n{data}")
f.close()

# 3. APPEND - Add more data
f = open("students.txt", "a")
f.write("New student added - Roll 74\n")
f.close()
print("Appended data")

# 4. READ LINE BY LINE
f = open("students.txt", "r")
print("\nLine by line:")
for line in f:
    print(f"-> {line.strip()}")
f.close()

# 5. WITH - Auto close (Best practice - BTech level)
print("\nUsing with (auto close):")
with open("students.txt", "r") as f:
    content = f.read()
    print(content)

# 6. WRITE list of numbers
my_list = [9,41,13,74,3,15]
with open("numbers.txt", "w") as f:
    for n in my_list:
        f.write(f"{n}\n")
print(f"Wrote list {my_list} to numbers.txt")

# 7. READ numbers and sum
with open("numbers.txt", "r") as f:
    total = 0
    for line in f:
        total += int(line.strip())
    print(f"Sum from file: {total}") # 155

# 8. Check file exists
import os
if os.path.exists("students.txt"):
    print("\nstudents.txt exists")
    print(f"Size: {os.path.getsize('students.txt')} bytes")

# 9. Practical - Save table of 6
with open("table6.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"6 x {i} = {6*i}\n")
print("\nTable of 6 saved to table6.txt")
