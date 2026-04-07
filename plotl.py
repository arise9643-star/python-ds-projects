import pandas as pd
import plotly.express as px
df = pd.read_csv("train.csv")
survival_count = df["Survived"].value_counts().reset_index()
fig = px.bar(survival_count, x = "Survived",  y = "count" , title= "Survival")
fig.show()