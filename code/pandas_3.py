import pandas as pd

# let's import a little bit of data
# i'm going to use the read_csv method
df = pd.read_csv("weather.csv", sep=",")
print(df.index)
print(df.columns)
print(df.head(10))
print(df.describe())

# drop missing information
# by default this will drop a row if any data is missing
# df = df.dropna()
# df = df.fillna(0)

# df.dropna(axis=1)
# print(df.max(), df.min(), df.mean())
print(df[0:10])

print(df["NAME"].unique())