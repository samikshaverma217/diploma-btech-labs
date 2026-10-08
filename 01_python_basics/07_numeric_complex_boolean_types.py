# Series 07 - All Remaining Data Types
# Numeric: int, float, complex + Boolean + NoneType

# 1. INT - Integer
a = 42
b = 54
print(f"INT: a={a}, b={b}, Type: {type(a)}")
print(f"Sum: {a+b}") # 96 from your lab
print(f"Sub: {a-b}")
print(f"Mul: {a*b}")
print(f"Div: {a/b}")
print(f"Floor Div: {a//b}")
print(f"Mod: {a%b}")
print(f"Power: {a**2}")

# 2. FLOAT - Decimal
p = 120.0
r = 4.5
t = 2.0
si = p * r * t / 100
print(f"\nFLOAT: P={p}, R={r}, T={t}")
print(f"SI = {si}, Type: {type(si)}") # 10.8

price = 99.99
print(f"Price: {price}, Int part: {int(price)}, Round: {round(price)}")

# 3. COMPLEX - a + bj (Important for Data Science)
c1 = 3 + 4j
c2 = 2 + 5j
print(f"\nCOMPLEX: c1={c1}, c2={c2}, Type: {type(c1)}")
print(f"Real of c1: {c1.real}") # 3.0
print(f"Imag of c1: {c1.imag}") # 4.0
print(f"Addition: {c1 + c2}") # (5+9j)
print(f"Subtraction: {c1 - c2}") # (1-1j)
print(f"Multiplication: {c1 * c2}") # (-14+23j)
print(f"Conjugate of c1: {c1.conjugate()}") # (3-4j)

# Complex from your numbers
z = complex(9, 41)
print(f"Complex from 9,41: {z}")
print(f"Magnitude: {abs(z):.2f}") # sqrt(9^2+41^2)

# 4. BOOLEAN - True/False
is_pass = True
is_fail = False
print(f"\nBOOLEAN: is_pass={is_pass}, Type: {type(is_pass)}")
print(f"True + True = {True + True}") # 2 - bool is subclass of int
print(f"True + False = {True + False}") # 1
print(f"10 > 5: {10 > 5}") # True
print(f"41 in [9,41,13,74]? {41 in [9,41,13,74]}") # True

# Boolean with conditions
marks = 74
print(f"Marks {marks} >= 40? {marks >= 40}") # True

# 5. NONETYPE - None
x = None
print(f"\nNONETYPE: x={x}, Type: {type(x)}")
print(f"Is None? {x is None}") # True

# 6. Type Conversion between numeric types
print("\n--- Type Conversion ---")
num_int = 15
num_float = float(num_int)
num_complex = complex(num_int)
print(f"Int {num_int} -> Float {num_float} -> Complex {num_complex}")

num_str = "54"
num_from_str = int(num_str)
print(f"String '{num_str}' -> Int {num_from_str}")

# 7. All numeric types in one list - like your lab [9,41,13,74,3,15]
mixed = [9, 41.5, 3+4j, True, 15]
print(f"\nMixed numeric list: {mixed}")
for item in mixed:
    print(f"  {item} -> {type(item).__name__}")
