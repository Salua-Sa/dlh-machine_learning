#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

fig = plt.figure(figsize=(6.4, 4.8))
ax = fig.add_subplot(111, projection="3d")
u1 = pca_data[:, 0]
u2 = pca_data[:, 1]
u3 = pca_data[:, 2]
ax.scatter(u1, u2, u3, c=labels, cmap="plasma")
ax.set_xlabel("U1")
ax.set_ylabel("U2")
ax.set_zlabel("U3")
ax.set_title("PCA of Iris Dataset")
plt.show()
