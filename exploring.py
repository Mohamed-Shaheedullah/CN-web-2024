import pandas as pd

df = pd.read_csv("results.csv")

print(df)

df.info()


print(df.describe())

print(df["home_score"].value_counts(normalize=True) * 100)


mask = df['home_score'] > 6

df = df[~mask] # squiggle means not

print(df["home_score"].mean())

################################ activity####################
######## goalscorers file##########

df2 = pd.read_csv("goalscorers.csv")

print(df2.head())

df2.info()

## some missing data from 'minute' column
## date may not be in datetime format

print(df2.describe())

## only one column of numerical data
## mean 50 minutes with a high SD as goal couldbe scored throughouit match.
## when analysing could use count to determine greatest goalscorers


####### shootouts #############

df3 = pd.read_csv("shootouts.csv")

print(df3.head())

df3.info()

## many 'first shooter' missing values

## when analysing could use counts to see who is most winners 

