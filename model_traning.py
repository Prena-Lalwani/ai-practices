from abc import ABC, abstractmethod
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris


class MLModel(ABC):
    def __init__(self):
        self.model = None

    @abstractmethod
    def train(self, X_train, y_train):
        pass

    @abstractmethod
    def predict(self, X_test):
        pass

    def evaluate(self, X_test, y_test):
        prediction = self.predict(X_test)
        acc = accuracy_score(y_test, prediction)
        return acc


class LogisticModel(MLModel):
    def __init__(self):
        super().__init__()
        self.model = LogisticRegression(max_iter=200)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)


class DecisionTreeModel(MLModel):
    def __init__(self):
        super().__init__()
        self.model = DecisionTreeClassifier()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)


class IrisData:
    def __init__(self):
        iris = load_iris()
        self.X = iris.data
        self.y = iris.target

    def get_split(self, test_size=0.2):
        return train_test_split(self.X, self.y, test_size=test_size, random_state=42)


if __name__ == "__main__":
    # Load data
    data = IrisData()
    X_train, X_test, y_train, y_test = data.get_split()

    # Try different models (Polymorphism in action)
    models = [LogisticModel(), DecisionTreeModel()]

    for model in models:
        model.train(X_train, y_train)
        acc = model.evaluate(X_test, y_test)
        print(f"{model.__class__.__name__} Accuracy: {acc:.2f}")
