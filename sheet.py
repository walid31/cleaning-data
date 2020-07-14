import pandas as pd
import numpy as np

# Create a dataframe of the csv file
df = pd.read_csv("Datasets/BL-Flickr-Images-Book.csv")
# print(df.head())

# Drop unuseful columns
to_drop =['Edition Statement',
          'Corporate Author',
          'Corporate Contributors',
          'Former owner',
          'Engraver',
          'Contributors',
          'Issuance type',
          'Shelfmarks']

df.drop(to_drop, axis = 1, inplace = True)
# print(df.head())

# Check if Identifier is unique to set it as the index of our df
if df['Identifier'].is_unique:
    df = df.set_index('Identifier')
# print(df.head())

# Let's do label-based indexing of random row
# print(df.loc[480])

# Position-based indexing
# print(df.iloc[0])

print(df.get_dtype_counts())

print(df.loc[1905:, 'Date of Publication'].head(10))

# A particular book can have only one date of publication
extr = df['Date of Publication'].str.extract(r'^(\d{4})', expand = False)
# print(extr.head())

print(df['Date of Publication'].isnull().sum() / len(df))
# get the numerical version
df['Date of Publication'] = pd.to_numeric(extr)
print(df['Date of Publication'].dtype)

nan_mean = df['Date of Publication'].isnull().sum() / len(df)

print(nan_mean)


