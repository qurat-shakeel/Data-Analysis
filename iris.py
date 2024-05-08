# -*- coding: utf-8 -*-
"""iris.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UKvpIovdWLLtUJwCPthwvBKZB8dZw6ei
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
Iris = pd.read_csv("Iris.csv")
Iris

# print datapoints and features
print(Iris.shape)

# column name in dataset
print(Iris.columns)

# data points for each class which are present
# number of flowers for which each species are present
Iris["Species"].value_counts()

# scatter plot
Iris.plot(kind='scatter' , x='SepalLengthCm' , y='SepalWidthCm')
plt.show()

#pair plot
plt.close()
sns.set_style("whitegrid")
sns.pairplot(Iris, hue = "Species", size = 3,diag_kind ="kde" )
plt.show()

import numpy as np
iris_setosa = Iris.loc[Iris["Species"]=="setosa"]
iris_virginica = Iris.loc[Iris["Species"] == "virginica"]
iris_versicolor = Iris.loc[Iris["Species"]== "versicolor"]

plt.plot(iris_setosa["PetalLengthCm"]), np.zeros_like(iris_setosa['PetalLengthCm'])
plt.plot(iris_virginica["PetalLengthCm"]), np.zeros_like(iris_virginica['PetalLengthCm'])
plt.plot(iris_versicolor["PetalLengthCm"]), np.zeros_like(iris_versicolor['PetalLengthCm'])
plt.show()

g=sns.FacetGrid(Iris, hue = "Species", height=5)
g.map(sns.distplot, "PetalLengthCm")
g.add_legend()
plt.show()

g=sns.FacetGrid(Iris, hue = "Species", height=5)
g.map(sns.distplot, "PetalWidthCm")
g.add_legend()
plt.show()

g=sns.FacetGrid(Iris, hue = "Species", height=5)
g.map(sns.distplot,"SepalLengthCm")
g.add_legend()
plt.show()

g=sns.FacetGrid(Iris, hue = "Species", height=5)
g.map(sns.distplot,"SepalWidthCm")
g.add_legend()
plt.show()

# means, Variance, Standard deviation
print("Means:")
print(np.mean(iris_setosa["PetalLengthCm"]))
# Mean with an outlier
print(np.mean(np.append(iris_setosa["PetalLengthCm"],50)))
print(np.mean(iris_virginica["PetalLengthCm"]))
print(np.mean(iris_versicolor["PetalLengthCm"]))

print("\n Standard Deviation")
print(np.std(iris_setosa["PetalLengthCm"]))
print(np.std(iris_virginica["PetalLengthCm"]))
print(np.std(iris_versicolor["PetalLengthCm"]))

# median, quantiles, percentiles, IQR
print("Median:")
print(np.median(iris_setosa["PetalLengthCm"]))
# median with an outlier
print(np.median(np.append(iris_setosa["PetalLengthCm"],50)))
print(np.median((iris_virginica["PetalLengthCm"])))
print(np.median((iris_versicolor["PetalLengthCm"])))

import numpy as np

print("\n Quantiles:")
print(np.percentile(iris_setosa["PetalLengthCm"],np.arange(0,100,25)))
print(np.percentile(iris_virginica["PetalLengthCm"],np.arange(0,100,25)))
print(np.percentile(iris_versicolor["PetalLengthCm"],np.arange(0,100,25)))

# Check if the DataFrames are empty
print("Number of rows in iris_setosa:", len(iris_setosa))
print("Number of rows in iris_virginica:", len(iris_virginica))
print("Number of rows in iris_versicolor:", len(iris_versicolor))

# Check if the column "PetalLengthCm" exists in each DataFrame
print("Columns in iris_setosa:", iris_setosa.columns)
print("Columns in iris_virginica:", iris_virginica.columns)
print("Columns in iris_versicolor:", iris_versicolor.columns)

# Check unique values in the "PetalLengthCm" column
print("Unique values in iris_setosa['PetalLengthCm']:", iris_setosa["PetalLengthCm"].unique())
print("Unique values in iris_virginica['PetalLengthCm']:", iris_virginica["PetalLengthCm"].unique())
print("Unique values in iris_versicolor['PetalLengthCm']:", iris_versicolor["PetalLengthCm"].unique())