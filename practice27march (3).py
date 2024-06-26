# -*- coding: utf-8 -*-
"""Practice27March.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZrpN4qX3Q_NziZfz9quYqsYnkxy8IaYR
"""

import pandas as pd
df = pd.read_csv('train.csv')
df



import pandas as pd

# Identify null values
null_values = df.isnull()

# Count null values
null_counts = null_values.sum()

print("Null values in each column:")
print(null_counts)

import pandas as pd
# Drop row with null values in the 'Embarked' column

df_clean = df.dropna(subset=['Embarked'])

import pandas as pd
# Calculate the mean age
mean_age = df['Age'].mean()

# Impute missing 'Age' values with the mean
df['Age'] = df['Age'].fillna(mean_age)

# Verify that null values are filled
print(df['Age'].isnull().sum())  # Should output 0 if all null values are filled

import pandas as pd
mean_age = df['Age'].mean()
print("Mean age: ",mean_age)

new_df = df.copy() # create a copy of original data Frame
new_df['Age'] = new_df['Age'].fillna(mean_age)
print(new_df)



import pandas as pd
embarked_counts_q = df[df['Embarked'] == 'Q']
print("Number of passengers embarked at Queenstown : ", len(embarked_counts_q))

import pandas as pd
embarked_counts_s = df[df['Embarked'] == 'S']
print(" Number of passengers embarked at Southampton : ", len(embarked_counts_s))

import pandas as pd
embarked_counts_c = df[df['Embarked'] == 'C']
print("Number of passengers embarked at Cherbourg : ",len(embarked_counts_c) )

import pandas as pd
import matplotlib.pyplot as plt

embarked_counts = df['Embarked'].value_counts()

embarked_counts.plot(kind='bar')

plt.title('Passenger count by Embarked City')
plt.xlabel('Embarked City')
plt.ylabel('Passenger Count')
plt.show()

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

all_colors = mcolors.CSS4_COLORS
print(all_colors.keys())

import pandas as pd
import matplotlib.pyplot as plt

embarked_counts = df['Embarked'].value_counts()
custom_colors = ['grey', 'orchid','orange']
# create a pie chart
plt.figure(figsize=(5,5))

plt.pie(embarked_counts, labels = embarked_counts.index,autopct = '%1.1f%%', startangle=180, colors=custom_colors )

plt.title('Percentage of passengers by embarked city')

plt.axis('equal')  # equal aspect ratio ensures pie as drawn as a circle

plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

numerical_cols = df.select_dtypes(include=['float64','int64'])
correlation_matrix = numerical_cols.corr()  # calculates correlation coefficients

plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap = 'coolwarm',fmt=".3f")
plt.title('Correlation matrix of Numerical Variables')
plt.show()

# different colormaps
import matplotlib.pyplot as plt

print(plt.colormaps())