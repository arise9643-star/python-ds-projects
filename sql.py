import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("train.csv")
engine = create_engine("sqlite:///titanic.db")
df.to_sql("passengers", engine, if_exists="replace", index=False)
print("Database created")
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///titanic.db")

cabins = pd.DataFrame({
    'PassengerId': [1, 2, 3, 4, 5],
    'CabinType': ['Economy', 'Luxury', 'Economy', 'Luxury', 'Economy'],
    'Deck': ['C', 'A', 'C', 'B', 'C']
})

cabins.to_sql("cabins", engine, if_exists="replace", index=False)
print("done")