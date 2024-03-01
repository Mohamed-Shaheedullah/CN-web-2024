import pandas as pd
import openpyxl

df = pd.read_excel('books.xlsx')

# print(df.head())

max_price = df["Price"].max()

print(f"The max price is {max_price}")

# Count the cells greater than 5
four_stars = (df['Rating / 5'] == 4).sum()

print(f"The number with four stars is {four_stars}")

# # john's soln
# four_stars_books = df.query("'Rating / 5' == 4")
# print(four_stars_books.shape[0])


mean_price = df["Price"].mean()

print(f"The mean price is {round(mean_price,2)}")
