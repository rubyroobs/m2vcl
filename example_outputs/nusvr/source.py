from sklearn.svm import NuSVR
import numpy as np
import m2vcl

n_samples, n_features = 10, 5
np.random.seed(0)
y = np.random.randn(n_samples)
X = np.random.randn(n_samples, n_features)
regr = NuSVR(C=1.0, nu=0.1)
regr.fit(X, y)
print(m2vcl.export_to_vcl(regr))
