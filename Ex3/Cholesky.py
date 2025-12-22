import math
import numpy as np

def Cholesky(matrix , n ):

    L = np.zeros((n, n))

    for i in range(n):
        for j in range (i+1):
            Sum = 0
            if(i==j):
                # Δικος μου κωδικας

                # for z in range(j):
                #     Sum += pow(matrix[j][z],2)
                # L[i,i] = numpy.sqrt(matrix[i][i] - Sum)

                #Βοηθεια απο Chatgpt
                Sum = sum(L[j][k] ** 2 for k in range(j))
                L[i][i] = np.sqrt(matrix[j][j] - Sum)
            else :
                # Δικος μου κωδικας

                # for z in range(j):
                #     Sum += (L[i][z] * L[j][z])

                #     L[i][j] = int((matrix[i][j] - Sum) /
                #                                L[j][j]);
                # Βοηθεια απο gpt
                Sum = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (matrix[i][j] - Sum) / L[j][j]
    return L

n = 3;
matrix = np.array([[6, 15, 55],
                   [15, 55, 225],
                   [55,225,979]])
L= Cholesky(matrix, n);
print(L)