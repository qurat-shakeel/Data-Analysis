# -*- coding: utf-8 -*-
"""extract_titles.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hQOrMrpPP87qjpDNX-EUdwVzJWRIYaei
"""

import pandas as pd
df=pd.read_csv('train.csv')
df

# extracting titles from names
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
df

# Create FamilySize feature
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df

# calculating fare per person
df['FarePerPerson'] = df['Fare'] / df['FamilySize']
df

# Extract Deck from Cabin
df['Deck'] = df['Cabin'].str.slice(0, 1)
df