import numpy as np
from sklearn.cluster import KMeans
# X = np.array( [[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]] )


def findmaxElem(cList, c_num):
    cdict = {}
    for i in range(c_num):
        cdict[i] = 0
    for num in cList:
        cdict[num] += 1
    # sort by count
    d = [(v, k) for k, v in cdict.items()]
    d.sort()
    return(d[-1][1])


X = np.array([[529.0, 0.95993108],
              [537.0, 0.92502451],
              [536.0, 0.94247776],
              [530.0, 0.97738439],
              [447.0, 1.2391838],
              [534.0, 0.9075712],
              [530.0, 0.94247776],
              [443.0, 1.2566371],
              [532.0, 0.92502451]])


c_num = 2
kmeans = KMeans(n_clusters=c_num, random_state=0).fit(X)


print(kmeans.labels_)
l_list = kmeans.labels_


print(findmaxElem(l_list, c_num))
print(kmeans.cluster_centers_)


#kmeans.predict([[0, 0], [4, 4]])
# array([[1.,  2.],
#       [4.,  2.]])

# print('hoge')
#
#
# print('test1')
#pca = PCA(n_components=2)
# pca.fit(X)
# PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
#    svd_solver='auto', tol=0.0, whiten=False)
# print(pca.explained_variance_ratio_)
# print(pca.components_)
#
# print('test2')
#pca = PCA(n_components=2, svd_solver='full')
# pca.fit(X)
# PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
#    svd_solver='full', tol=0.0, whiten=False)
# print(pca.explained_variance_ratio_)
# print(pca.components_)
#
# print('test3')
#pca = PCA(n_components=1, svd_solver='arpack')
# pca.fit(X)
# PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
#    svd_solver='arpack', tol=0.0, whiten=False)
# print(pca.explained_variance_ratio_)
# print(pca.components_)
