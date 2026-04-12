import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("train.csv")
sns.countplot( x = "Survived", data = df)
plt.title("Survived count")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.show()
sns.barplot(x= "Pclass", y = "Fare", data = df)
plt.title("avg fare")
plt.show()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)  
plt.title("Correlation Heatmap")
plt.show()
sns.histplot(x="Age", data = df)
plt.title("Age")
plt.show()