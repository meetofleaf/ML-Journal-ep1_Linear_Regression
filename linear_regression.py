### Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


### Import Dataset
dataset = pd.read_csv('student_marks.csv')    # Feel free to use your own data by replacing filename in quotes with your data filename.


### Data preprocessing
# Calculating study time per course for each student. This can also be used as independent variable.
#dataset['study_time_per_course'] = dataset['time_study'] / dataset['number_courses']

# Columns in order after adding the new variable/column: number_courses, time_study, Marks, study_time_per_course

# Extracting independent (X) and dependent (y) columns/fields/variables. You can experiment with different independent variables.
X = dataset.iloc[:,1:2].values   # time_study
y = dataset.iloc[:,2].values    # Marks
# Reference for iloc: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html


### Splitting the dataset into training and test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


### Training the model
from sklearn.linear_model import LinearRegression

# Training the Linear Regression model (named regressor here) on the training set
regressor = LinearRegression()      # Define regressor as linear regression model
regressor.fit(X_train, y_train)     # Train the model on training data of both independent and dependent data OR
                                    # you could simply say, teaching the model using the training data OR
                                    # fit the model on the training data, hence function name 'fit'


### Prediction
# Predicting the dependent values using the test set of independent data
y_pred = regressor.predict(X_test)
# Simply, after learning from training data, the model tries to predict the dependent data (y_pred) from independent data (X_test)

# Function to predict marks based on input using previously trained model (regressor)
def predictor(input_value):
    return regressor.predict([[input_value]])

print(predictor(3)) # Based on the independent data that you've set, change the input value from 3 (default) to any value you like.
                    # For eg. if you chose to use study time (time_study) as independent variable, then you could enter any reasonable time in hours (1.5, 5, 7 etc.)


### You're done with the Machine Learning part, now let's visualize our results


### Visualizing the model
# Visualizing Training Results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Marks vs Study time')
plt.xlabel('Study time')
plt.ylabel('Marks')
plt.show()

# Visualizing Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Marks vs Study time ')
plt.xlabel('Study time')
plt.ylabel('Marks')
plt.show()

