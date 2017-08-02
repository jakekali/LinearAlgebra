import numpy as np
import math


def getMagnitude(vector1):
    vector1 = np.reshape(vector1,-1)
    vector2 = np.array([])
    total = 0
    i = 0
    for num in vector1:
        vector2 = np.append(vector2, vector1[i] ** 2)
        total = total + (vector1[i] ** 2)
        i = i + 1
    return math.sqrt(total)
