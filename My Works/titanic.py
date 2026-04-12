import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("train.csv")
gender_survival = df.groupby("Sex")["Survived"].mean()
plt.bar(gender_survival.index, gender_survival.values)
plt.xlabel("gender")
plt.ylabel("survival rate")
plt.title("survival by sex")
plt.show()
pclass_survival = df.groupby("Pclass")["Survived"].mean()
plt.bar(pclass_survival.index,pclass_survival.values)
plt.xlabel("Class")
plt.ylabel("Survival Rate")
plt.title("Survival by class")
plt.show()
df = df.dropna(subset=["Age"])
plt.hist(df[df['Survived']==1]['Age'], bins=30, color='blue', label='Survived')
plt.hist(df[df['Survived']==0]['Age'], bins=30, color='red', label='Died')
plt.legend()
plt.xlabel("Age")
plt.ylabel("Survival rate")
plt.title("Survival by age")
plt.show()
summary = pd.DataFrame({
    'metric': ['overall_survival', 'female_survival', 'male_survival', 'class1_survival', 'class2_survival', 'class3_survival'],
    'value': [
        df['Survived'].mean(),
        gender_survival['female'],
        gender_survival['male'],
        pclass_survival[1],
        pclass_survival[2],
        pclass_survival[3]
    ]
})
summary.to_csv("titanic_summary.csv", index=False)
