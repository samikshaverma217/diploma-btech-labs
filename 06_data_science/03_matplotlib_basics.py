# Series 17 - Matplotlib - Graphs & Charts
# BTech Lab compulsory
import matplotlib.pyplot as plt
import numpy as np

# 1. Simple Line - Table of 2
x = [1,2,3,4,5,6,7,8,9,10]
y = [2*i for i in x]
plt.plot(x, y)
plt.title("Table of 2")
plt.xlabel("Number")
plt.ylabel("2 x Number")
plt.savefig("table2_plot.png")
plt.close()
print("Saved table2_plot.png")

# 2. Marks Bar Chart - From your rolls
rolls = [9,41,13,74,3,15,42,54]
marks = [74,85,62,91,45,78,88,69]
plt.bar(rolls, marks, color='skyblue')
plt.title("Student Marks")
plt.xlabel("Roll No")
plt.ylabel("Marks")
plt.savefig("marks_bar.png")
plt.close()
print("Saved marks_bar.png")

# 3. Pie Chart
labels = ['Pass', 'Fail']
sizes = [6, 2]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['green','red'])
plt.title("Pass/Fail Ratio")
plt.savefig("pie_pass.png")
plt.close()
print("Saved pie_pass.png")

# 4. Scatter Plot
p = [120,200,150,100,300,120,200,150]
si = [9.6,20,18,12,9,9.6,30,12]
plt.scatter(p, si, color='red')
plt.title("P vs SI (R=4,T=2)")
plt.xlabel("Principal (P)")
plt.ylabel("SI")
plt.savefig("scatter_si.png")
plt.close()
print("Saved scatter_si.png")

# 5. Multiple Lines - Tables 2,3,6
x = np.arange(1,11)
y2 = x*2
y3 = x*3
y6 = x*6
plt.plot(x, y2, label='Table 2', marker='o')
plt.plot(x, y3, label='Table 3', marker='s')
plt.plot(x, y6, label='Table 6', marker='^')
plt.title("Tables 2,3,6 Comparison")
plt.xlabel("1 to 10")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.savefig("tables_comparison.png")
plt.close()
print("Saved tables_comparison.png")

# 6. Subplots
fig, axs = plt.subplots(2, 2, figsize=(8,6))
axs[0,0].plot(x, y2)
axs[0,0].set_title("Table 2")
axs[0,1].bar(rolls, marks)
axs[0,1].set_title("Marks")
axs[1,0].pie(sizes, labels=labels, autopct='%1.1f%%')
axs[1,0].set_title("Pass/Fail")
axs[1,1].scatter(p, si)
axs[1,1].set_title("P vs SI")
plt.tight_layout()
plt.savefig("dashboard.png")
plt.close()
print("Saved dashboard.png - Full dashboard!")

print("\nAll plots saved! Check files.")
