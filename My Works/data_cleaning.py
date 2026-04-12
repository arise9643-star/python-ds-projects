import pandas as pd
df = pd.read_csv("train.csv")
print(df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
before = len(df)
df = df.drop_duplicates()
print("Duplicates removed:", before - len(df))
Q1 = df["Fare"].quantile(0.25)
Q3 = df["Fare"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df = df[(df["Fare"] >= lower) & (df["Fare"] <= upper)]
print(df)
