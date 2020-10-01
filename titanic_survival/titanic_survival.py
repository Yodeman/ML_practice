import pandas as pd
import numpy as np
#from sklearn.model_selection import train_test_split
#from sklearn.tree import DecisionTreeClassifier

train_data = pd.read_csv("train.csv")
#print(train_data["Name"][:10])
X_test = np.asarray(pd.read_csv("test.csv"))

def get_title():
	title = []
	for name in train_data['Name']:
		title.append(name.split()[1])
	return title

title = get_title()
print(title[:10])

target = np.array(train_data["Survived"])

#X_train = np.array(train_data.drop("Survived", axis=1))
#print(X_train.head())

#clf = DecisionTreeClassifier()
#clf.fit(X_train, target)

#prediction = clf.predict(X_test)
#print("Accuracy on training set: {}".format(clf.score(X_train, target)))
#print("Prediction:\n", prediction[:10])