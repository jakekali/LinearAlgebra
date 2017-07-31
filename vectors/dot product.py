import numpy as np

def dotProduct(vector1, vector2):
    vector1 = np.reshape(vector1,-1)
    vector2 = np.reshape(vector2,-1)

    if(vector1.size != vector2.size):
        return bool(0)
    dots = np.array([])
    i = 0;
    for num in vector1:
        dots = np.append(dots, num * vector2[i])
        print (str(num) + "("+ str(vector2[i])+") + ")
        i = i + 1

    print(str(dots))
    fin = 0
    for num in dots:
        fin = fin + num
    print(str(fin))
    return (fin)

#2 Vectors are right, if they there inter product is 0
def isRight(vector1,vector2):
    if dotProduct(vector1 ,vector2) == int(0):
        return True
    else:
        return False

vector1 = np.array([6,2])
vector2 = np.array([[-1],[5]])

print(isRight(vector1, vector2))
