import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv("train.csv")
df.dropna(inplace=True)
convert = {"male": 0,
           "female": 1}
df["sex_no"] = df["Sex"].map(convert)
X = df[["Pclass","sex_no","Age"]]
Y = df["Survived"]
X_train , X_test , Y_train , Y_test = train_test_split(X,Y, random_state=42)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train,Y_train)
accuracy = model.predict(X_test)
print(accuracy_score(Y_test,accuracy))
