import pandas as pd

df = pd.read_csv('population_data.csv')

print(df.head())
s = df.country_name.value_counts()
print(s)
print(df.shape)