import numpy as np

data = np.genfromtxt(
    "breast-cancer.csv",
    delimiter=",",
    dtype=str,
    encoding="utf-8",
    skip_header=1
)

print("Data shape:", data.shape)

diagnosis = data[:, 1]

X = data[:, 2:].astype(float)

print("X shape:", X.shape)
print("Diagnosis shape:", diagnosis.shape)

'''
X.shape
Returns the dimensions of the array.
X[:, i]
Selects column i from the numerical feature matrix.
np.max()
Finds the largest value.
np.min()
Finds the smallest value.
np.mean()
Calculates the average.
np.sum(condition)
Counts values satisfying a Boolean condition because True is treated as 1 and False as 0.
array[condition]
Performs Boolean filtering and selects only values for which the condition is True.
np.std()


Calculates standard deviation.
np.argmax()
Returns the index/position of the maximum value.
np.unique()
Finds unique values; with return_counts=True it also returns their frequencies.
'''
