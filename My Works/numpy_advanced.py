import pandas as pd
import numpy as np
df = pd.read_csv("train.csv")
df = df.dropna(subset="Survived")
df["Survived_Status"] = np.where(df["Survived"] == 1 ,"Survived","Died")
mask = df["Fare"] > 100
print(df[mask])
def fare(a):
    if a < 20:
        return "budget"
    elif a > 20 and a < 100:
        return "mid"
    else:
        return "luxury"
vectorized = np.vectorize(fare)
df["Fare_Range"] = vectorized(df["Fare"].values)
print(df)

