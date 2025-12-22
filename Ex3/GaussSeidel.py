import numpy as np

MAX = 5000
n = 50
eps = 1e-4

def gaussSeidel(A,b,x):
    for k in range(MAX):
        old = np.zeros(n)

        for i in range(n):
            Sum = 0.0
            for j in range(n):
                if j != i :
                    Sum += A[i][j] * x[j]
            old[i] = 1.0/A[i][i] *(b[i]- Sum)
        error = max(abs(old-x))
        x[:]= old

        if error <  eps:
            break

    print("Λυση για Gauss Seidel :")
    for i in range(n):
        print(f"{x[i]:.6f}")

# Αρχικοποιηση Πινακων

A = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if i == j:
            A[i][j] = 5
        elif (i > 1 and i > j + 1) or (j > 1 and j > i + 1):
            A[i][j] = 0
        else:
            A[i][j] = -2
b = np.zeros(n)
for i in range(n):
    if i==0 or i== n-1:
        b[i]= 3.0
    else :
        b[i]=1.0
x= np.zeros(n)


gaussSeidel(A,b,x)
