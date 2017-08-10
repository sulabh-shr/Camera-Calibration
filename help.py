import numpy as np

a = np.array([[0, 0, 4, 6],
              [5, 0, 0, 1],
              [8, 0, 2, 0],
             [0, 11, 0, 7]])

nonzero_indices = a.nonzero()
nonzero_a = a[a.nonzero()]

print('Non-zero row and column indices respectively: ', nonzero_indices)
print('Non-zero row indices: ', nonzero_indices[0])
print('Non-zero col indices: ', nonzero_indices[1])
print('Non-zero a elements: ', nonzero_a)
