# Series 03 - String Operations
# Words: banana, polytechnic, khushi

word = "banana"
print(f"Word: {word}")
print(f"Length: {len(word)}")  # 6

# Check substring - from your lab
print(f"'nan' in 'banana': {'nan' in word}")  # True

# Case conversion
print(f"Lower: {word.lower()}")
print(f"Upper: {word.upper()}")
print(f"Capitalized: {word.capitalize()}")

# Second word from your lab
text = "polytechnic"
print(f"\nText: {text}")
print(f"Upper: {text.upper()}")
print(f"Contains 'poly': {'poly' in text}")

# Find position - from your lab: find 'khushi' = 6
name = "khushi"
sentence = "hello khushi"
pos = sentence.find(name)
print(f"\nFind '{name}' in '{sentence}': {pos}")  # 6

# Slice example
print(f"First 3 chars of banana: {word[:3]}")  # ban
