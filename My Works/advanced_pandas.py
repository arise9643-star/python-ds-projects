import pandas as pd
df = pd.read_csv("train.csv")
df = df.dropna(subset="Age")
df["Fare_filter"] = df["Fare"].apply(lambda filter: "high" if filter > 50  else "low")
df["Age_group"] = df["Age"].apply(lambda group: "Child" if group < 18 else "Senior" if group > 60 else "Adult")
print(df[["Name","Fare","Fare_filter","Age","Age_group"]].head(10))
