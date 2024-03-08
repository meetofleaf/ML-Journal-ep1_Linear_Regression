import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


dataset = pd.read_csv('M:\STUDY\Datasets\Kaggle\student_marks.csv')


# Calculating study time per course for each student
#dataset['study_time_per_course'] = dataset['time_study'] / dataset['number_courses']

# COLUMNS: number_courses, time_study, Marks, study_time_per_course

# Extracting Independent (X) and dependent set (y)
X = dataset.iloc[:,1:2].values   # time_study
y = dataset.iloc[:,2].values    # Marks


# Splitting the dataset into training and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
print(X)
print(y)


# Train the Linear Regression model on the training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# Predicting the dependent values using test set results
y_pred = regressor.predict(X_test)


### You're done with the Machine Learning part, now let's visualize our result

# Visualizing Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Marks vs Study time per Course')
plt.xlabel('Study time per Course')
plt.ylabel('Marks')
plt.show()

# Visualizing Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Marks vs Study time per Course')
plt.xlabel('Study time per Course')
plt.ylabel('Marks')
plt.show()


# Function to predict marks based on input study time per course using previously trained regressor
def predictor(study_time_per_course):
    return regressor.predict([[study_time_per_course]])

print(predictor(3))
