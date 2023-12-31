# -*- coding: utf-8 -*-
"""Simple_linear_regression.ipynb

Original file is located at
    https://colab.research.google.com/drive/1KfsvrQxVt8aQe1XcZFsosA5hbBnwkJBS

# Simple Linear Regression

## Importing the libraries
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""## Importing the dataset"""

dataset = pd.read_csv("Salary_Data.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size = 0.2,random_state = 0)

"""## Training the Simple Linear Regression model on the Training set"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

"""## Predicting the Test set results"""

y_pred = regressor.predict(x_test)

"""## Visualising the Training set results"""

plt.scatter(x_train,y_train,color= 'red')
plt.plot(x_test,regressor.predict(x_test),color ='blue')
plt.title("Salary VS Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

"""## Visualising the Test set results"""

plt.scatter(x_test,y_test,color = 'red')
plt.plot(x_test,regressor.predict(x_test),color = 'blue')
plt.title("Salary VS Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
