import numpy as np
def directSum(martix1,martix2):
    rows = martix1.shape[0] + martix2.shape[0]
    col = martix1.shape[1] + martix2.shape[1]
    dd = np.ndarray(shape=(rows, col))
    dd.fill(0)
    rm1 = 0
    for rows in martix1:
        cm1 = 0
        for colms in rows:
            dd[rm1][cm1] = martix1[rm1][cm1]
            cm1 = cm1 + 1
        rm1 = rm1 + 1
    rml = martix1.shape[0]
    for rows in martix2:
        cm1 = martix1.shape[1]
        for colms in rows:
            dd[rm1][cm1] = martix2[rm1 - martix1.shape[0]][cm1 - martix1.shape[1]]
            cm1 = cm1 + 1
        rm1 = rm1 + 1
    print(dd)

d = np.array([
    [1,2,3,4],
    [3,4,3,4],
    [3, 4, 3, 4]
])
dd = np.array([
    [1,6,3,6,6],
    [2,3,5,6,6],
    [2, 3, 5, 6, 6]

])
directSum(d,dd)