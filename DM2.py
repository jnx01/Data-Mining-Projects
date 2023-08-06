import pandas as pd
import numpy as np

def PCA_func(X, num_components):

    #Step 1: centering data
    X_centered = X - np.mean(X, axis=0)

    #Step 2: calculate covariance matrix
    cov_mat = np.cov(X_centered, rowvar=False)

    #Step 3: find eigen values and corresponding eigen vectors
    eigen_values, eigen_vectors = np.linalg.eigh(cov_mat)

    #Step 4: sorting eigen values and eigen vectors to find N most significant eigen values and their corresponding eigen vectors
    sorted_index = np.argsort(eigen_values)[::-1]           #Descending order
    sorted_eigenvalue = eigen_values[sorted_index]
    sorted_eigenvectors = eigen_vectors[:, sorted_index]

    #Step 5: selecting 'num_components' subset from the eigen vectors
    eigenvector_subset = sorted_eigenvectors[:, 0:num_components]

    #Step 6: performing dot product to reduce data
    X_reduced = np.dot(eigenvector_subset.transpose(), X_centered.transpose()).transpose()

    return X_reduced


path = r'/home/jahanzebnaeem/Downloads/DM/Project-20092022-124505am/iris.csv'
data = pd.read_csv(path)

x = data.iloc[:, 0:4]
target = data.iloc[:, 4]
reduced_matrix = PCA_func(x, 2)

final_df = pd.DataFrame(reduced_matrix, columns=['PC1', 'PC2'])
final_df = pd.concat([final_df, pd.DataFrame(target)], axis=1)
print('Result from own PCA function:\n')
print(final_df, '\n\n')






import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def PCA_func(X, num_components):

    #Step 1: centering data
    X_centered = X - np.mean(X, axis=0)

    #Step 2: calculate covariance matrix
    cov_mat = np.cov(X_centered, rowvar=False)

    #Step 3: find eigen values and corresponding eigen vectors
    eigen_values, eigen_vectors = np.linalg.eigh(cov_mat)

    #Step 4: sorting eigen values and eigen vectors to find N most significant eigen values and their corresponding eigen vectors
    sorted_index = np.argsort(eigen_values)[::-1]           #Descending order
    sorted_eigenvalue = eigen_values[sorted_index]
    sorted_eigenvectors = eigen_vectors[:, sorted_index]

    #Step 5: selecting 'num_components' subset from the eigen vectors
    eigenvector_subset = sorted_eigenvectors[:, 0:num_components]

    #Step 6: performing dot product to reduce data
    X_reduced = np.dot(eigenvector_subset.transpose(), X_centered.transpose()).transpose()

    return X_reduced


path = r'/home/jahanzebnaeem/Downloads/DM/Project-20092022-124505am/iris.csv'
allData = pd.read_csv(path)
data = allData.iloc[:, 0:4]
reduced_data= PCA_func(data, 2)                         # reducing to 2 dimensions so that we can plot easily
colors = ['red', 'green', 'blue', 'black', 'yellow']

for i in range(1, 6):
    labels = KMeans(n_clusters=i, random_state=3).fit_predict(X=reduced_data)
    unique_labels = list(set(labels))

    for j in unique_labels:
        filtered_label = reduced_data[labels == int(j)]
        plt.scatter(filtered_label[:, 0], filtered_label[:, 1], color=colors[int(j)])
    plt.show()
