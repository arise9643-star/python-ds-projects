import plotly.express as px
import pandas as pd
df = pd.read_csv("train.csv")
fig = px.scatter(df ,x="Age",y="Fare",color="Survived",title="Age vs Fare")
fig.show()
hist = px.histogram(df,x="Age",title="age distribution")
hist.show()
survived_rate = df["Survived"].value_counts().reset_index()
bar = px.bar(survived_rate,x="Survived",title="survived")
bar.show()
box = px.box(df,x="Pclass",y="Age",title="pclass vs age")
box.show()
