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

    return (fin)


vector1 = np.array([4,-2,0,1])
vector2 = np.array([[-1],[-3],[1],[5]])

print(dotProduct(vector1, vector2))
