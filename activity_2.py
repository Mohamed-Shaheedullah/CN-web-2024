import pandas as pd
import openpyxl

df = pd.read_excel('books.xlsx')

# print(df.head())

max_price = df["Price"].max()

print(f" the max price is {max_price}")

# Count the cells greater than 5
four_stars = (df['Rating / 5'] == 4).sum()

print(f"The number with four stars is {four_stars}")

mean_price = df["Price"].mean()

print(f"The mean price is {round(mean_price,2)}")
