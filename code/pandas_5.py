import pandas as pd
import matplotlib.pyplot as plt

# let's import a little bit of data
# i'm going to use the read_csv method
df = pd.read_csv("weather.csv", sep=",")

df = df[df['TMAX'].notnull()]
df = df[df["TMIN"].notnull()]

df["TAVG"] = df[['TMAX', 'TMIN']].mean(1)
rotterdam_df = df[df["NAME"] == "ROTTERDAM, NL"]

# convert date to a datetime object
rotterdam_df["DATE"] = pd.to_datetime(rotterdam_df["DATE"])
rot = rotterdam_df.set_index("DATE")
rot["TMAX"].plot()
plt.show()
# print(df)