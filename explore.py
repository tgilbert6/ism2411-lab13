# Exercise 1
print("\n--- Exercise 1 ---\n")

import pandas as pd

df= pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# Exercise 2
print("\n--- Exercise 2 ---\n")

south = df[df['region'] == 'South']
print(len(south))
print(south.head())

# Exercise 3
print("\n--- Exercise 3 ---\n")

print(df.sort_values('revenue', ascending=False).head(5))

# Exercise 4
print("\n--- Exercise 4 ---\n")

big_south = df[(df['region']=='South') & (df['revenue']>1000)]
print(big_south[1:5])