import numpy as np


def martixMultiply(martix1, martix2):
    # check if the two martixs can be multiplied together

    if martix1.shape[1] != martix2.shape[0]:
        return bool(0)
    martix2 = np.swapaxes(martix2,0,1)

    vals = np.array([])
    for row1 in martix1:
        for col2 in martix2:
            val = 0
            i = 0
            for num in row1:

                val = (num * col2[i]) + val
                i = i + 1
            vals = np.append(vals,val)

    return vals.reshape(martix1.shape[0],martix2.shape[0])


