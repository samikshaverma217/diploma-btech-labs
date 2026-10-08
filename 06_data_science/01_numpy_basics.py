# Series 15 - NumPy Basics
# BTech Previous Sem - Important for placements
import numpy as np

# 1. Array - Like list but faster
arr = np.array([9,41,13,74,3,15])
print(f"Array: {arr}")
print(f"Type: {type(arr)}")

# 2. From your lab numbers
marks = np.array([42,54,74,41,15,9])
print(f"\nMarks: {marks}")
print(f"Mean: {np.mean(marks)}")
print(f"Max: {np.max(marks)}")
print(f"Min: {np.min(marks)}")
print(f"Sum: {np.sum(marks)}") # 235

# 3. 2D Array - Matrix
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"\nMatrix:\n{matrix}")

# 4. Zeros, Ones, Range
print(f"\nZeros 3: {np.zeros(3)}")
print(f"Ones 3x3:\n{np.ones((3,3))}")
print(f"Range 1-10: {np.arange(1,11)}")
print(f"Linspace: {np.linspace(1,10,5)}")

# 5. Operations - Fast
arr1 = np.array([120,4,2])
arr2 = np.array([10,2,1])
print(f"\narr1: {arr1}")
print(f"arr2: {arr2}")
print(f"Add: {arr1+arr2}")
print(f"Multiply: {arr1*arr2}")
print(f"Square: {arr1**2}")

# 6. Indexing & Slicing
print(f"\narr[0]: {arr[0]}")
print(f"arr[1:4]: {arr[1:4]}")
print(f"arr > 20: {arr[arr>20]}")

# 7. Reshape
arr_6 = np.arange(1,7)
print(f"\nOriginal: {arr_6}")
print(f"Reshape 2x3:\n{arr_6.reshape(2,3)}")

# 8. SI Calculation using NumPy - P=120,R=4,T=2
P = np.array([120, 200, 300])
R = np.array([4, 5, 6])
T = np.array([2, 3, 2])
SI = (P*R*T)/100
print(f"\nP:{P}, R:{R}, T:{T}")
print(f"SI: {SI}")

# 9. Random - For projects
print(f"\nRandom 3 numbers: {np.random.randint(1,100,3)}")
