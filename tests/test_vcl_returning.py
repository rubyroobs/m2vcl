import unittest

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris, load_boston
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import NuSVR
import numpy as np
import m2vcl


class TestVCLReturning(unittest.TestCase):

    def test_vcl_returning_for_boston_linear_regression(self):
        boston = load_boston()
        X, y = boston.data, boston.target
        estimator = LinearRegression()
        estimator.fit(X, y)

        self.assertNotEqual(m2vcl.export_to_vcl(estimator), "")

    def test_vcl_returning_for_iris_decision_tree(self):
        iris = load_iris()
        X = iris.data
        y = iris.target
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, random_state=0)

        clf = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
        clf.fit(X_train, y_train)
        self.assertNotEqual(m2vcl.export_to_vcl(clf), "")

    def test_vcl_returning_for_nusvr(self):
        n_samples, n_features = 10, 5
        np.random.seed(0)
        y = np.random.randn(n_samples)
        X = np.random.randn(n_samples, n_features)
        regr = NuSVR(C=1.0, nu=0.1)
        regr.fit(X, y)
        self.assertNotEqual(m2vcl.export_to_vcl(regr), "")


if __name__ == '__main__':
    unittest.main()
