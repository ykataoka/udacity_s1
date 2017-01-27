import numpy as np
from sklearn.decomposition import PCA
# X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

print('hoge')

X = np.array([[529.0, 0.95993108],
              [537.0, 0.92502451],
              [536.0, 0.94247776],
              [530.0, 0.97738439],
              [447.0, 1.2391838],
              [534.0, 0.9075712],
              [530.0, 0.94247776],
              [443.0, 1.2566371],
              [532.0, 0.92502451]]
             )

print('test1')
pca = PCA(n_components=2)
pca.fit(X)
PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
    svd_solver='auto', tol=0.0, whiten=False)
print(pca.explained_variance_ratio_)
print(pca.components_)

print('test2')
pca = PCA(n_components=2, svd_solver='full')
pca.fit(X)
PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
    svd_solver='full', tol=0.0, whiten=False)
print(pca.explained_variance_ratio_)
print(pca.components_)

print('test3')
pca = PCA(n_components=1, svd_solver='arpack')
pca.fit(X)
PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
    svd_solver='arpack', tol=0.0, whiten=False)
print(pca.explained_variance_ratio_)
print(pca.components_)
