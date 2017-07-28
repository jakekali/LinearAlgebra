import numpy as np

def add(martix1, martix2):
    if(martix1.shape != martix2.shape):
            return bool(0)
    new = np.full_like(martix1, 1)


    rowNum = 0
    for row in martix1:
        colNum = 0
        for col in row:
            new[rowNum][colNum] = martix1[rowNum][colNum] + martix2[rowNum][colNum]
            print (rowNum,colNum)
            colNum = colNum + 1
        rowNum = rowNum + 1

    return new

def sub(martix1, martix2):
    if(martix1.shape != martix2.shape):
            return bool(0)
    new = np.full_like(martix1, 1)


    rowNum = 0
    for row in martix1:
        colNum = 0
        for col in row:
            new[rowNum][colNum] = martix1[rowNum][colNum] - martix2[rowNum][colNum]
            print (rowNum,colNum)
            colNum = colNum + 1
        rowNum = rowNum + 1

    return new

array1 = np.array([ [5,3,4,4],
                    [5,3,4,4]
                            ])

array2 = np.array([[-4,3,4,4],
                   [5,3,4,4]])

print(add(array1,array2))

