# -*- coding: utf-8 -*-
"""TitanicRegressionAnalysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T2gBzNfistRm_rOOzLrf6GJdt--gLIzb
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


df = pd.read_csv('train.csv')

df

features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = df[features]
y = df['Survived']

numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, ['Age', 'SibSp', 'Parch', 'Fare']),
        ('cat', categorical_transformer, ['Pclass', 'Sex', 'Embarked'])
    ])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model training

lr_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('classifier', LogisticRegression(random_state=42))])

lr_pipeline.fit(X_train, y_train)

linreg_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                  ('regressor', LinearRegression())])

linreg_pipeline.fit(X_train, y_train)

# model Evaluation

lr_predictions = lr_pipeline.predict(X_test)

print("Logistic Regression Classification Report:")
print(classification_report(y_test, lr_predictions))

linreg_predictions = linreg_pipeline.predict(X_test)
linreg_predictions = np.where(linreg_predictions >= 0.5, 1, 0)

print("Linear Regression as Classifier Report:")
print(classification_report(y_test, linreg_predictions))