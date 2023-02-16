import os
import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X = iris.data
y = iris.target

rf = RandomForestClassifier()
rf.fit(X,y)

rf.predict(X)
joblib.dump(rf, "./django_app/prediction/ml/IRISRFClassifier.joblib")