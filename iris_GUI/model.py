from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = load_iris()
feature_names = data.feature_names
target_names = data.target_names

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

clf = LogisticRegression(max_iter=1000, random_state=0)
clf.fit(X_train, y_train)

