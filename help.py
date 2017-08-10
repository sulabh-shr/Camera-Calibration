import numpy as np

a = np.array([[0, 0, 4, 6],
              [5, 0, 0, 1],
              [8, 0, 2, 0],
             [0, 11, 0, 7]])

"""
    NON-ZERO
"""
nonzero_indices = a.nonzero()
nonzero_a = a[a.nonzero()]

print('\nNON-ZERO')
print('Non-zero row and column indices: ', nonzero_indices)
print('Non-zero row indices: ', nonzero_indices[0])
print('Non-zero col indices: ', nonzero_indices[1])
print('Non-zero a elements: ', nonzero_a)


"""
    SUM AXIS
"""

sum_rows = np.sum(a, axis=0)
sum_cols = np.sum(a, axis=1)

print('\nSUM-AXIS')
print('Sum of rows: ', sum_rows)
print('Sum of cols: ', sum_cols)
assert sum_rows.shape == sum_cols.shape, 'Index size not same'


"""
    DSTACK
"""
b = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])
c = np.array([['a', 'b', 'c', 'd'],
              ['e', 'f', 'g', 'h'],
              ['i', 'j', 'k', 'l']])

stacked = np.dstack((b, c))
print('\nDSTACK')
print('Stacked output: \n', stacked)
print('Stacked shape: ', stacked.shape)
print('(num_rows, num_cols, number_stacked_arrays)')

