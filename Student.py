import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("student.csv")
total = df["name"].nunique()
a = {
    "A" : 4,
    "B" : 3,
    "C" : 2,
    "D"  : 1,
    "F"  : 0
}
df["grade_score"] = df["grade"].map(a)
avg = df["grade_score"].mean()
highest = df.groupby("name")["grade_score"].mean().sort_values(ascending=False).head(1)
lowest = df.groupby("name")["grade_score"].mean().sort_values(ascending=False).tail(1)
grouped = df.groupby("name")["grade_score"].mean()
less_average = df[df["grade_score"]< avg]
print(f"total number of students : {total}")
print(f"grade to score = {df["grade_score"]}")
print(f"average score in grade is {avg}")
print(f"the highest students are {highest}")
print(f"the lowest average score : {lowest}")
print(f"the people who scored below average are : {less_average}")
plt.bar(grouped.index,grouped.values)
plt.xlabel("Name")
plt.ylabel("Grade score")
plt.title("Students")
plt.show()