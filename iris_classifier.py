"""
Iris Flower Classifier
------------------------
A ML project that demonstrates:
- Python OOP
- Basic ML workflow using scikit-learn
- Train/test split, model training, and evaluation

Dataset: the classic Iris dataset (built into scikit-learn, no download needed)
Goal: predict the species of an iris flower from 4 measurements
(sepal length, sepal width, petal length, petal width)
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


class IrisClassifier:
    """A small wrapper class around a scikit-learn model.

    This demonstrates OOP: encapsulating data + model + logic
    inside a single reusable object.
    """

    def __init__(self, test_size=0.2, random_state=42):
        self.test_size = test_size
        self.random_state = random_state
        self.model = DecisionTreeClassifier(random_state=random_state)
        self.feature_names = None
        self.target_names = None

    def load_data(self):
        """Load the Iris dataset and split into train/test sets."""
        data = load_iris()
        self.feature_names = data.feature_names
        self.target_names = data.target_names

        X_train, X_test, y_train, y_test = train_test_split(
            data.data,
            data.target,
            test_size=self.test_size,
            random_state=self.random_state,
        )
        self.X_train, self.X_test = X_train, X_test
        self.y_train, self.y_test = y_train, y_test

    def train(self):
        """Train the decision tree model on the training data."""
        self.model.fit(self.X_train, self.y_train)

    def evaluate(self):
        """Evaluate the model on the test set and print results."""
        predictions = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, predictions)

        print(f"Accuracy: {accuracy:.2%}\n")
        print("Classification report:")
        print(classification_report(
            self.y_test, predictions, target_names=self.target_names
        ))

    def predict_sample(self, measurements):
        """Predict the species for a single new flower.

        measurements: list of 4 numbers
            [sepal_length, sepal_width, petal_length, petal_width]
        """
        prediction = self.model.predict([measurements])[0]
        return self.target_names[prediction]


if __name__ == "__main__":
    clf = IrisClassifier()
    clf.load_data()
    clf.train()
    clf.evaluate()

    # Try predicting a brand new flower measurement
    sample = [5.1, 3.5, 1.4, 0.2]
    result = clf.predict_sample(sample)
    print(f"Prediction for sample {sample}: {result}")
