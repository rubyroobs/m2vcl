from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

import m2vcl

boston = load_boston()
X, y = boston.data, boston.target
estimator = LinearRegression()
estimator.fit(X, y)
print(m2vcl.export_to_vcl(estimator))
