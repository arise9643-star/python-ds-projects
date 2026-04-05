import pandas as pd
import matplotlib.pyplot as plt
print("Expense Tracker")
data = []
while True:
    catogary = input("Enter category (or 'done' to finish): ").lower()
    if catogary == "done":
        break
    amount = float(input("Enter the amount: "))
    data.append([catogary,amount])
income = int(input("How much was your income: "))
df = pd.DataFrame(data , columns=["Catogary","Amount"] )
df.to_csv("tracker.csv", index =False)
total_spent = df["Amount"].sum()
tax = 15/100 * income
savings = income - total_spent - tax
percentage = total_spent/income * 100
print(f"You have spent a total of {total_spent} without tax")
print(f"you have a spent a total of {total_spent + tax} with tax")
print(f"you have saved {savings} which is {percentage} of your income")
plt.bar(df["Catogary"] , df["Amount"])
plt.axhline(y=df['Amount'].mean(), color='green', linestyle='--', label='Avg')
plt.legend()
plt.title("Expense Tracker")
plt.xlabel("Catogary")
plt.ylabel("Amount")
plt.show()
plt.pie(df["Amount"], labels=df["Catogary"],autopct="%1.1f%%")
plt.title("Amount used")
plt.show()

