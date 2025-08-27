from abc import ABC, abstractmethod
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from data_handler import texts, labels


class MLModel(ABC):

    @abstractmethod
    def train(self, X_train, y_train):
        pass

    @abstractmethod
    def predict(self, X_test):
        pass

    def evaluate(self, X_test, y_test):
        preds = self.predict(X_test)
        return accuracy_score(y_test, preds)


class NaiveBayes(MLModel):
    def __init__(self):
        self.model = MultinomialNB()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)


class ReviewData:
    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels
        self.vectorizer = CountVectorizer()

    def get_split(self, test_size=0.2):
        X = self.vectorizer.fit_transform(self.texts)
        return train_test_split(X, self.labels, test_size=test_size, random_state=42)


if __name__ == "__main__":
    # Load data
    data = ReviewData(texts, labels)
    X_train, X_test, y_train, y_test = data.get_split()

    # Try different models (Polymorphism in action)
    models = [NaiveBayes()]

    for model in models:
        model.train(X_train, y_train)
        acc = model.evaluate(X_test, y_test)
        print(f"{model.__class__.__name__} Accuracy: {acc:.2f}")
