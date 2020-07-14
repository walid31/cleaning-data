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
print(df.iloc[1])





