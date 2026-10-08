# Series 16 - Pandas Basics
# Most asked in BTech Interviews
import pandas as pd

# 1. Series - 1D
data = [9,41,13,74,3,15]
s = pd.Series(data)
print(f"Series:\n{s}")
print(f"\nMean: {s.mean()}, Sum: {s.sum()}")

# 2. DataFrame - 2D Table - Like Excel
students = {
    "Roll": [9,41,13,74,3,15,42,54],
    "Name": ["A","B","C","D","E","F","G","H"],
    "Marks": [74,85,62,91,45,78,88,69]
}
df = pd.DataFrame(students)
print(f"\nDataFrame:\n{df}")

# 3. Head, Tail, Info
print(f"\nHead 3:\n{df.head(3)}")
print(f"\nTail 2:\n{df.tail(2)}")
print(f"\nShape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

# 4. Selecting Columns
print(f"\nOnly Marks:\n{df['Marks']}")
print(f"\nRoll & Marks:\n{df[['Roll','Marks']]}")

# 5. Filtering - Important
print(f"\nMarks > 75:\n{df[df['Marks']>75]}")
print(f"\nRoll == 74:\n{df[df['Roll']==74]}")

# 6. Adding Column - SI from your lab P=120,R=4,T=2
df['P'] = [120,200,150,100,300,120,200,150]
df['R'] = [4,5,4,6,3,4,5,4]
df['T'] = [2,2,3,2,1,2,3,2]
df['SI'] = (df['P']*df['R']*df['T'])/100
print(f"\nWith SI Column:\n{df}")

# 7. Sorting
print(f"\nSorted by Marks:\n{df.sort_values('Marks', ascending=False)}")

# 8. GroupBy & Stats
print(f"\nMarks Stats:")
print(df['Marks'].describe())

# 9. Read CSV - Real world use
# df_csv = pd.read_csv("students.csv")
# For demo creating csv
df.to_csv("students_pandas.csv", index=False)
print("\nSaved to students_pandas.csv")

df_read = pd.read_csv("students_pandas.csv")
print(f"\nRead from CSV:\n{df_read.head()}")

# 10. Fill NA, Drop
df2 = pd.DataFrame({"A":[1,2,None,4], "B":[None,2,3,4]})
print(f"\nWith NA:\n{df2}")
print(f"Drop NA:\n{df2.dropna()}")
print(f"Fill NA with 0:\n{df2.fillna(0)}")
