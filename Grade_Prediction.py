# import tensorflow as tf
import pandas as pd 
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as pyplot
from matplotlib import style
import pickle

data = pd.read_csv(r'C:\Users\Dell\Documents\myenv\Machine Learning\LinearRegression\Students data\student-mat.csv', sep = ";")

# print(data.head)

data = data[["G1", "G2", "G3", "absences", "failures", "studytime"]]
# print()
# print(data.head)

predict = "G3"

x = np.array(data.drop([predict], axis=1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.1)


# best = 0
# for i in range(30):
#     x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.1)

#     linear = linear_model.LinearRegression()
#     linear.fit(x_train, y_train)

#     accu = linear.score(x_test, y_test)
#     print("Accuracy of our model is: ", accu*100, "%")

#     if(best < accu):
#         best = accu
#         with open ("StudentModel.pickle", "wb") as f:
#             pickle.dump(linear, f)

pickle_in = open(r"C:\Users\Dell\Documents\myenv\Machine Learning\LinearRegression\StudentModel.pickle", "rb")
linear = pickle.load(pickle_in)

predictions = linear.predict(x_test)
print("\nCoeffecients = ", linear.coef_) #Coeffecients of linear Regression model
print("Intercept = ", linear.intercept_ , "\n")  #Intercept of linear Regression model

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

p = "G1"
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade (G3)")
pyplot.show()