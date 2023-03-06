import pandas as pd

# let's import a little bit of data
# i'm going to use the read_csv method
df = pd.read_csv("weather.csv", sep=",")

df['TMAX'].notnull()
df['TMAX'].notnull().value_counts()

df = df[df['TMAX'].notnull()]
df = df[df["TMIN"].notnull()]

hot = df[df['TMAX'] > 28]

rot = df[df['NAME'] == "ROTTERDAM, NL"]
df["TAVG"] = df[['TMAX', 'TMIN']].mean(1)
# print(df)