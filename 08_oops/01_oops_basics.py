# Series 19+20 - COMPLETE OOPS - BTech Core
# Class, Object, Constructor Overriding, super(), All Inheritance Types, Polymorphism, Encapsulation, Abstraction

# ========== 1. CLASS & OBJECT ==========
class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Roll: {self.roll}, Name: {self.name}, Marks: {self.marks}")

s1 = Student(9, "Samiksha", 74)
s1.display()
s2 = Student(41, "Khushi", 85)
s2.display()

# ========== 2. SI Calculator Class - Your Lab P=120,R=4,T=2 ==========
class SICalculator:
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t
    def calculate(self):
        return (self.p * self.r * self.t) / 100

si_obj = SICalculator(120, 4, 2)
print(f"\nSI: {si_obj.calculate()}") # 9.6

# ========== 3. CONSTRUCTOR OVERRIDING ==========
print("\n=== CONSTRUCTOR OVERRIDING ===")
class Parent:
    def __init__(self):
        print("Parent Constructor - P=120, R=4, T=2")

class Child(Parent):
    def __init__(self): # Overrides Parent
        print("Child Constructor Overriding Parent")

Child()

# ========== 4. super() FUNCTION ==========
print("\n=== super() - Calling Parent ===")
class Parent2:
    def __init__(self, p, r):
        self.p = p
        self.r = r
        print(f"Parent: P={p}, R={r}")
    def display(self):
        print("Parent Display")

class Child2(Parent2):
    def __init__(self, p, r, t):
        super().__init__(p, r) # Calls Parent constructor
        self.t = t
        print(f"Child: T={t}")
    def display(self):
        super().display() # Calls parent method
        print("Child Display - Overridden")
    def si(self):
        return (self.p * self.r * self.t)/100

obj = Child2(120, 4, 2)
print(f"SI = {obj.si()}")
obj.display()

# ========== 5. TYPES OF INHERITANCE ==========

# A. SINGLE - One parent, one child
print("\n=== 5A. SINGLE INHERITANCE ===")
class College:
    def __init__(self):
        print("College: Diploma BTech")
class StudentSingle(College):
    def __init__(self, roll):
        super().__init__()
        print(f"Student Roll: {roll}")
StudentSingle(9)

# B. MULTILEVEL - Grandparent -> Parent -> Child
print("\n=== 5B. MULTILEVEL ===")
class GrandParent:
    def __init__(self):
        print("GrandParent: Foundation")
class ParentML(GrandParent):
    def __init__(self):
        super().__init__()
        print("Parent: Middle Layer")
class ChildML(ParentML):
    def __init__(self):
        super().__init__()
        print("Child: Final - Roll 74")
ChildML()

# C. MULTIPLE - Two parents, one child
print("\n=== 5C. MULTIPLE ===")
class Father:
    def __init__(self):
        print("Father: Roll 9,41,13")
    def skills_father(self):
        print("Father Skills: Maths")
class Mother:
    def __init__(self):
        print("Mother: Marks 74,85,69")
    def skills_mother(self):
        print("Mother Skills: Science")
class ChildMultiple(Father, Mother):
    def __init__(self):
        super().__init__()
        Mother.__init__(self)
        print("Child: Inherits both")
    def show(self):
        self.skills_father()
        self.skills_mother()
ChildMultiple().show()

# D. HIERARCHICAL - One parent, many children
print("\n=== 5D. HIERARCHICAL ===")
class Teacher:
    def __init__(self, name):
        self.name = name
        print(f"Teacher: {name}")
class Student1(Teacher):
    def __init__(self, name, roll):
        super().__init__(name)
        print(f"Student1 Roll: {roll}")
class Student2(Teacher):
    def __init__(self, name, roll):
        super().__init__(name)
        print(f"Student2 Roll: {roll}")
Student1("Samiksha", 74)
Student2("Khushi", 41)

# E. HYBRID - Mix
print("\n=== 5E. HYBRID ===")
class A:
    def showA(self): print("Class A - Roll 9")
class B(A):
    def showB(self): print("Class B - Roll 41")
class C(A):
    def showC(self): print("Class C - Roll 13")
class D(B, C):
    def showD(self): print("Class D - Inherits B,C,A")
d = D()
d.showA(); d.showB(); d.showC(); d.showD()

# ========== 6. ENCAPSULATION - Private __ ==========
print("\n=== 6. ENCAPSULATION ===")
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
acc = BankAccount(120)
acc.deposit(4)
print(f"Balance: {acc.get_balance()}")

# ========== 7. POLYMORPHISM - Same name diff behavior ==========
print("\n=== 7. POLYMORPHISM ===")
class Table:
    def table(self, n):
        print(f"Table of {n}: {n*1}, {n*2}, {n*3}...")
class Table6(Table):
    def table(self): # Override
        n=6
        print(f"Table of {n} (Overridden):")
        for i in range(1,6):
            print(f"{n} x {i} = {n*i}")
Table().table(2)
Table6().table()

# ========== 8. ABSTRACTION ==========
print("\n=== 8. ABSTRACTION ===")
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r
class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side * self.side
print(f"Circle r=6 area: {Circle(6).area()}")
print(f"Square side=9 area: {Square(9).area()}")

# ========== 9. REAL LAB EXAMPLE - Constructor Chaining ==========
print("\n=== 9. REAL LAB CHAINING ===")
class Person:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
class Marks(Person):
    def __init__(self, name, roll, marks):
        super().__init__(name, roll)
        self.marks = marks
class Result(Marks):
    def __init__(self, name, roll, marks):
        super().__init__(name, roll, marks)
        self.total = sum(marks)
    def display(self):
        print(f"Result {self.name} Roll {self.roll}: Total {self.total}, Avg {self.total/len(self.marks)}")

Result("Samiksha", 74, [74,41,13,9,15]).display()

print("\n=== COMPLETE OOPS COVERED ===")
