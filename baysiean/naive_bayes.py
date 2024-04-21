import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


data=pd.read_csv('decision_tree.csv')



X=data.drop('PlayTennis',axis=1)
y=data['PlayTennis']

X=pd.get_dummies(X)



X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=101)


clf=GaussianNB()


clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

print(y_pred)

accuracy_score=accuracy_score(y_test,y_pred)



print(accuracy_score)

print(classification_report(y_test,y_pred))