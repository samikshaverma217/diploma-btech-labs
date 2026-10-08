# Series 18 - Database Connectivity
# SQLite - No setup needed, works everywhere
# MySQL code also added in comment

import sqlite3

# 1. CONNECT & CREATE TABLE
conn = sqlite3.connect("college.db")
cur = conn.cursor()
print("Connected to college.db")

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER,
    branch TEXT
)
""")
print("Table students created")

# 2. INSERT - Using your lab data
# Clear old data
cur.execute("DELETE FROM students")

students_data = [
    (9, "Samiksha", 74, "CSE"),
    (41, "Khushi", 85, "CSE"),
    (13, "Aman", 62, "ECE"),
    (74, "Rahul", 91, "CSE"),
    (3, "Priya", 45, "ME"),
    (15, "Ankit", 78, "CSE"),
    (42, "Neha", 88, "ECE"),
    (54, "Vikash", 69, "CSE")
]

cur.executemany("INSERT INTO students VALUES (?,?,?,?)", students_data)
conn.commit()
print(f"Inserted {len(students_data)} students")

# 3. SELECT - Read all
print("\n--- All Students ---")
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for r in rows:
    print(r)

# 4. SELECT with WHERE - Filter
print("\n--- CSE Branch Only ---")
cur.execute("SELECT * FROM students WHERE branch='CSE'")
for r in cur.fetchall():
    print(r)

# 5. SELECT - Marks > 75
print("\n--- Marks > 75 ---")
cur.execute("SELECT name, marks FROM students WHERE marks > 75 ORDER BY marks DESC")
for r in cur.fetchall():
    print(r)

# 6. UPDATE
cur.execute("UPDATE students SET marks=90 WHERE roll=9")
conn.commit()
print("\nUpdated roll 9 marks to 90")

# 7. DELETE
cur.execute("DELETE FROM students WHERE roll=3")
conn.commit()
print("Deleted roll 3")

# 8. Final Data
print("\n--- Final Data ---")
cur.execute("SELECT * FROM students")
for r in cur.fetchall():
    print(r)

# 9. SI Table - From your P=120,R=4,T=2
cur.execute("""
CREATE TABLE IF NOT EXISTS si_calc (
    p INTEGER,
    r INTEGER,
    t INTEGER,
    si REAL
)
""")
cur.execute("DELETE FROM si_calc")
p,r,t = 120,4,2
si = (p*r*t)/100
cur.execute("INSERT INTO si_calc VALUES (?,?,?,?)", (p,r,t,si))
conn.commit()
print(f"\nSI Saved: P={p},R={r},T={t},SI={si}")

cur.execute("SELECT * FROM si_calc")
print(cur.fetchall())

conn.close()
print("\nDB Closed - college.db saved!")

# 10. MySQL Version - For Viva (Commented)
"""
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)
cur = conn.cursor()
# Same queries work!
"""
