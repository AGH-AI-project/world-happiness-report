import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn import preprocessing
# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score
from sklearn.metrics import classification_report, confusion_matrix


names = ["Country","Happiness.Rank","Happiness.Score","Whisker.high","Whisker.low","Economy..GDP.per.Capita.","Family","Health..Life.Expectancy.","Freedom","Generosity","Trust..Government.Corruption.","Dystopia.Residual"]
data2015 = pd.read_csv('2015.csv')
data2016 = pd.read_csv('2016.csv')
data2017 = pd.read_csv('2017.csv', names = names)

X = data2017.iloc[:, [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11]]

Y = data2017.iloc[:, [2]]

data2015.head(50)
data2016.head(50)
data2017.head(50)

X.head()
Y.head()

le = preprocessing.LabelEncoder()
X = X.apply(le.fit_transform)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.20)
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
mlp.fit(X_train, y_train.values.ravel())
predictions = mlp.predict(X_test)
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

