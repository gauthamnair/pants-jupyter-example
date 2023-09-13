import numpy as np


def add_numbers_with_numpy(*xs):
    a = np.array(list(xs))
    return a.sum()