![Banner](.media/banner.png)
# ML Journal - Machine Learning Fundamentals Series
In this series of repositories, we'll explore various models, documenting the code and thought process behind each one.  The goal is to create a journal-like experience for both myself and anyone following along. By sharing the journey, we can:

- Break down complex concepts: We'll approach each model step-by-step, making the learning process manageable.
- Learn from mistakes: Documenting the process allows us to identify and learn from any errors along the way.
- Build a foundation: Each repository will build upon the knowledge from the previous one, creating a solid foundation in machine learning basics.
- We believe this approach can be particularly helpful for beginners struggling to find a starting point in the vast world of machine learning.


# Ep 01 - Linear Regression
This is the first addition in the 'ML Journal' series aimed at revisiting fundamental machine learning models. This specific repository focuses on Linear Regression, a widely used technique for modeling linear relationships between features and a target variable.

#### [Concept explanation](https://github.com/meetofleaf/ML-Journal-ep1_Linear_Regression/blob/main/linear_regression_explanation.md)

## Data
This repository includes the dataset (student_marks.csv) suitable for linear regression.
The dataset contains 3 variables and 100 instances and was uploaded by [M Yasser H](https://www.kaggle.com/yasserh) on [Kaggle](https://www.kaggle.com/).

Dataset link: https://www.kaggle.com/datasets/yasserh/student-marks-dataset

**Data dictionary**:
|Variable Name  |Data type |Variable type |Variable role |Sample   |
|:--------------|:---------|:-------------|:-------------|--------:|
|number_courses |int       |Discrete      |Independent   |_3_      |
|time_study     |float     |Continuous    |Independent   |_4.508_  |
|Marks          |float     |Continuous    |Dependent     |_19.202_ |


## Code
The Python code file (linear_regression.py) demonstrates how to implement linear regression using a popular machine learning library scikit-learn. You will find guiding comments in the code specifying purpose of each block of code in 1-2 lines.


## Requirements
Following is a list of the programs and libraries, with the versions, used in the code:

- `Python==3.12.1`
  - `pandas==2.2.0`
  - `numpy==1.26.3`
  - `matplotlib==3.8.3`
  - `scikit-learn==1.4.1`


## Getting Started
- Clone this repository.
- Make sure you have the required programs and libraries installed. You can install them using the requirements file with:
  - `pip install -r requirements.txt`
- Simply run the Python script either from your OS' command prompt or from your choice of IDE.
  - `py linear_regression.py`
- Follow the comments and code execution to understand the process.
- I encourage you to experiment with the code, modify the data, and play around with the model!
- Lastly, feel free to share any suggestions, corrections, ideas or questions you might have.

Also feel free to reach out to me for any discussion or collaboration. I'd be glad to productively interact with you.

This is just the first step in our machine learning journey. Stay tuned for future repositories exploring other fundamental models!


## References & Guidance Links:
- Python: https://www.python.org/
  - Scikit-learn: https://scikit-learn.org/stable/install.html
  - Pandas: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
  - NumPy: https://numpy.org/install/
  - Matplotlib: https://matplotlib.org/stable/users/installing/index.html
- Pip (Python Package Manager): https://pip.pypa.io/en/stable/user_guide/
- Git: https://git-scm.com/
