# Series 05 - Set Operations (All Operations)
# Set = No duplicate, Unordered

data = {9, 41, 13, 74, 3, 15}
print(f"Set: {data}") # Order can change
print(f"Count: {len(data)}") # 6

# 1. Adding elements
data.add(100)
print(f"\nAfter add 100: {data}")

data.update([200, 300])
print(f"After update [200,300]: {data}")

# 2. Removing elements
data.remove(100) # Error if not exists
print(f"\nAfter remove 100: {data}")

data.discard(500) # No error if not exists
print(f"After discard 500 (safe): {data}")

popped = data.pop() # Removes random
print(f"Popped element: {popped}")
print(f"Set now: {data}")
data.add(popped) # Add back for next operations

# 3. Set Operations - Very Important for BTech
set_a = {9, 41, 13, 74}
set_b = {13, 74, 3, 15}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")

print(f"\nUnion (A|B): {set_a | set_b}") # All elements
print(f"Intersection (A&B): {set_a & set_b}") # Common: 13,74
print(f"Difference (A-B): {set_a - set_b}") # Only in A
print(f"Difference (B-A): {set_b - set_a}") # Only in B
print(f"Symmetric Difference (A^B): {set_a ^ set_b}") # Not common

# 4. Membership
print(f"\nIs 41 in set_a? {41 in set_a}") # True
print(f"Is 100 in set_a? {100 in set_a}") # False

# 5. Subset / Superset
small = {9, 41}
print(f"\nIs {small} subset of {set_a}? {small.issubset(set_a)}") # True
print(f"Is {set_a} superset of {small}? {set_a.issuperset(small)}") # True

# 6. Clear
# data.clear() # Empties set
