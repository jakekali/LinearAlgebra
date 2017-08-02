import numpy as np
import math
import get1Magnitude as gm
import dot_product as dp
import math
def getAngle(vector1,vector2):

    mag1 = gm.getMagnitude(vector1)
    mag2 = gm.getMagnitude(vector2)
    dop = dp.dotProduct(vector1,vector2)

    cosx = dop / (mag1 * mag2)
    return math.degrees(math.acos(cosx))

vector1 = np.array([2,6])
vector2 = np.array([-1,5])

print(getAngle(vector1,vector2))