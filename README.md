# IRIS Classifier

A beginner-friendly Machine Learning project that classifies Iris flowers into their respective species using a Decision Tree Classifier with Python and Scikit-learn.

The project also demonstrates Object-Oriented Programming (OOP) by encapsulating the dataset, model, training, evaluation, and prediction logic inside a reusable `IrisClassifier` class.

---

## Overview

The Iris dataset is a classic Machine Learning dataset containing measurements of Iris flowers from three different species.

This project uses four measurements to predict the species of an Iris flower:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The implementation uses Scikit-learn's built-in Iris dataset, so no external dataset download is required.

---

## Features

* Iris flower species classification
* Decision Tree classification
* Python implementation
* Object-Oriented Programming structure
* Train/test data splitting
* Model accuracy evaluation
* Classification report
* Individual flower prediction
* Reusable classifier class

---

## Machine Learning Workflow

```text
Load Iris Dataset
       ↓
Split Data
       ↓
Train Decision Tree
       ↓
Evaluate Model
       ↓
Make Predictions
```

The dataset is divided into:

* 80% training data
* 20% testing data

A fixed `random_state=42` is used to make the train/test split reproducible.

---

## Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Programming language            |
| Scikit-learn  | Machine Learning                |
| Decision Tree | Classification algorithm        |
| OOP           | Model and workflow organization |

### Libraries Used

```python
scikit-learn
```

The project uses the following Scikit-learn components:

```python
load_iris
train_test_split
DecisionTreeClassifier
accuracy_score
classification_report
```

---

## Project Structure

```text
IRIS-classifier/
│
├── iris_classifier.py
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Hazammm/IRIS-classifier.git
```

### 2. Navigate to the project

```bash
cd IRIS-classifier
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
For this project only Scikit-learn is required.

---

## Usage

Run the Python script:

```bash
python iris_classifier.py
```

The program will:

1. Load the Iris dataset
2. Split the dataset into training and testing sets
3. Train the Decision Tree model
4. Evaluate the model
5. Display the classification report
6. Predict the species of a sample Iris flower

---

## Example Prediction

The project includes an example flower with the following measurements:

```python
[5.1, 3.5, 1.4, 0.2]
```

These represent:

```text
Sepal Length = 5.1
Sepal Width  = 3.5
Petal Length = 1.4
Petal Width  = 0.2
```

The model then predicts the corresponding Iris species.

---

## Object-Oriented Design

The project uses an `IrisClassifier` class to organize the Machine Learning workflow.

### Main Methods

| Method             | Purpose                              |
| ------------------ | ------------------------------------ |
| `load_data()`      | Loads and splits the Iris dataset    |
| `train()`          | Trains the Decision Tree model       |
| `evaluate()`       | Evaluates model performance          |
| `predict_sample()` | Predicts the species of a new flower |

This structure keeps the data, model, training process, evaluation, and prediction logic organized inside a reusable object.

---

## Model Evaluation

The project evaluates the classifier using accuracy and a classification report.

### Accuracy

Measures the percentage of correctly classified test samples.

```text
Accuracy = Correct Predictions / Total Predictions
```

### Classification Report

The classification report provides:

* Precision
* Recall
* F1-score
* Support

These metrics provide additional information about the classifier's performance for each Iris species.

---

## Why Decision Tree?

A Decision Tree was selected because it is:

* Easy to understand
* Suitable for classification tasks
* Simple to implement with Scikit-learn
* Interpretable

The model makes predictions by learning decision rules from the training data.

---

## Dataset

This project uses the Iris dataset provided directly by Scikit-learn.

The dataset contains four numerical features describing Iris flowers and three target classes representing different Iris species.

No manual dataset download is required.

---

## Learning Objectives

This project demonstrates fundamental Machine Learning concepts including:

* Dataset loading
* Feature and target separation
* Train/test splitting
* Supervised learning
* Classification
* Decision Trees
* Model evaluation
* Accuracy
* Precision
* Recall
* F1-score
* Single-sample prediction
* Object-Oriented Programming in Python

---

## Future Improvements

* Add confusion matrix visualization
* Add feature importance visualization
* Compare multiple classification algorithms
* Add hyperparameter tuning
* Add cross-validation
* Add model serialization
* Add automated tests
* Add CI/CD with GitHub Actions

---

## Limitations

This project is primarily designed for learning and demonstration purposes.

The Iris dataset is small and clean compared with real-world datasets, so performance on this dataset should not be treated as an indication of performance on complex production classification problems.

---

## License

This project is licensed under the MIT License.



