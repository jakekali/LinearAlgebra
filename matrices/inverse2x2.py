import numpy as np
import multiplyingMartices as mm
def inverse2x2(matrix1):
    diff = (matrix1[1][1] * matrix1[0][0])-  (matrix1[1][0] * matrix1[0][1])
    final =  np.array([
        [matrix1[1][1]/diff, (-1 * matrix1[0][1]) / diff],
        [(-1 * matrix1[1][0]) / diff, (1 * matrix1[0][0]) / diff],
    ])

    result = mm.martixMultiply(matrix1,final)

    id = np.array([[1,0],[0,1]])
    if(result.all() == id.all()):
        return final;

inverse2x2(np.array([[4,-7],[2,-3]]))