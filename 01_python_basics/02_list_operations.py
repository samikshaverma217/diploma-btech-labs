# Series 02 - List Operations [9,41,13,74,3,15]
# Diploma CSE Lab

data = [9,41,13,74,3,15]

print(f"List: {data}")
print(f"Count: {len(data)}")  # 6
print(f"Sum: {sum(data)}")  # 155
print(f"Max: {max(data)}")  # 74
print(f"Min: {min(data)}")  # 3
print(f"Average: {sum(data)/len(data):.2f}")  # 25.83

# Filter from your lab - numbers > 10
filtered = [x for x in data if x > 10]
print(f"Greater than 10: {filtered}")  # [41, 13, 74, 15]

# Even and Odd separate
evens = [x for x in data if x % 2 == 0]
odds = [x for x in data if x % 2 != 0]
print(f"Evens: {evens}")
print(f"Odds: {odds}")
