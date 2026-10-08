# Series 04 - Tuple Operations (All Operations)
# Tuple is immutable - from Diploma Lab

data = (9, 41, 13, 74, 3, 15, 9, 41) # Using your numbers
print(f"Tuple: {data}")

# 1. Basic operations
print(f"Count: {len(data)}") # 8
print(f"Sum: {sum(data)}") # 205
print(f"Max: {max(data)}") # 74
print(f"Min: {min(data)}") # 3

# 2. Indexing
print(f"\nFirst element: {data[0]}") # 9
print(f"Last element: {data[-1]}") # 41
print(f"Second last: {data[-2]}") # 9

# 3. Slicing
print(f"\nFirst 3: {data[:3]}") # (9, 41, 13)
print(f"Last 3: {data[-3:]}") # (15, 9, 41)
print(f"Middle: {data[2:5]}") # (13, 74, 3)

# 4. Count and Index - important for tuple
print(f"\nCount of 9: {data.count(9)}") # 2
print(f"Index of 74: {data.index(74)}") # 3

# 5. Membership
print(f"\nIs 13 in tuple? {13 in data}") # True
print(f"Is 100 in tuple? {100 in data}") # False

# 6. Unpacking - BTech level
a, b, c, d, e, f, g, h = data
print(f"\nUnpacked: a={a}, b={b}")

# 7. Convert Tuple to List and back
temp_list = list(data)
temp_list.append(100)
new_tuple = tuple(temp_list)
print(f"\nAfter adding 100: {new_tuple}")

# 8. Tuple with one element (interview question)
single = (5,)
print(f"\nSingle element tuple: {single} Type: {type(single)}")
