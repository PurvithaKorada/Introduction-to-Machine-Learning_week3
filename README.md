# InternNova – Week 3: Assignment 

## Overview

This repository contains the tasks and mini-project completed as part of Week 3 of the InternNova Artificial Intelligence and Python Internship.

The work focuses on understanding Machine Learning fundamentals, preparing datasets, performing data preprocessing, training a classification model, and making predictions using Python.

## Objectives

- Understand the fundamentals of Machine Learning.
- Learn the difference between Artificial Intelligence, Machine Learning, and Deep Learning.
- Understand supervised and unsupervised learning.
- Load and explore datasets using Pandas.
- Identify features and target variables.
- Perform data cleaning and preprocessing.
- Split datasets into training and testing sets.
- Build and evaluate a Machine Learning model.
- Develop a Student Performance Prediction mini-project.

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Tasks Completed

### Task 1: Machine Learning Fundamentals
Studied the basic concepts of Machine Learning, including datasets, features, labels, training and testing data, classification, regression, supervised learning, unsupervised learning, and real-world applications.

### Task 2: Dataset Preparation
Created and explored a Student Performance Dataset using Pandas.

Activities performed:
- Dataset loading
- Displaying the first five records
- Checking dataset shape and data types
- Identifying and handling missing values
- Selecting features and target variables

### Task 3: Train-Test Split and Data Preprocessing
Prepared the dataset for Machine Learning using Scikit-learn.

Activities performed:
- Label encoding
- Handling missing values
- Separating features and target
- Splitting the dataset into 80% training and 20% testing data

### Task 4: Building the First Machine Learning Model
Implemented a Decision Tree Classifier using Scikit-learn.

Activities performed:
- Model creation and training
- Making predictions
- Evaluating model accuracy
- Testing with a new student record

### Task 5: Mini Project – Student Performance Prediction
Developed a classification model to predict whether a student is likely to Pass or Fail.

**Input Features:**
- Study Hours
- Attendance
- Previous Marks
- Assignment Score

**Target Variable:** Result (Pass/Fail)

**Algorithm:** Decision Tree Classifier

The model was evaluated using accuracy score and tested with three new student records.

## Dataset

A synthetic Student Performance Dataset containing 100 sample records was created using Python.

The dataset is intended for educational and demonstration purposes and does not represent actual student records.

## Repository Structure

```text
week3/
│
├── Mini_Project/
├── Screenshots/
│
├── Dataset.csv
├── Student_Performance_Prediction...
├── Student_Performance_Raw.csv
│
├── Task1_ML_Fundamentals_Report...
├── Task2_Dataset_preparation_Expl...
├── Task3_Train-Test Split & Data Pr...
├── Task4_Explanation_How_The_M...
├── Task5_Student Performance Pre...
│
├── Week3_ML.ipynb
└── .gitattributes
```

## How to Run the Project

1. Clone or download this repository.
2. Install the required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib
```

3. Open `Week3_ML.ipynb` using Jupyter Notebook.
4. Run the notebook cells sequentially.

To execute the standalone mini-project:

```bash
python Student_Performance_Prediction.py
```

Ensure that `Dataset.csv` is available in the main repository folder.

## Learning Outcomes

- Understood basic Machine Learning concepts.
- Gained practical experience in dataset preparation and cleaning.
- Learned feature selection and target encoding.
- Performed train-test splitting using Scikit-learn.
- Trained and evaluated a Decision Tree classification model.
- Developed a basic student performance prediction system.

## Conclusion

This internship assignment provided practical exposure to Machine Learning using Python. It helped develop an understanding of the complete Machine Learning workflow, from dataset preparation and preprocessing to model training, prediction, and evaluation.

---

**Internship:** InternNova – Artificial Intelligence & Python Internship  
**Week:** 03  
**Project:** Student Performance Prediction
