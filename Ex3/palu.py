import numpy as np

def PALU(A,b):
    n = len(A)
    U = A
    L = np.identity(n)


    # LU αναλυση
    for i in range(n-1):
        for j in range(n):
            if j>i:
                L[j][i]=U[j][i]/U[i][i]
                for z in range(n):
                    U[j][z]-= L[j][i]*U[i][z]
    print(f"Ο πινακας L ειναι :\n {np.array(L)}")
    print("-------------------------------")
    print(f"Ο πινακας U ειναι :\n {np.array(U)}")
    print("-------------------------------")
    #Forward substitution Ly = b
    y = np.zeros(n)
    for i in range(n):
        Sum=0
        for j in range(n):
            if(i!=j):
                Sum += L[i,j]*y[j]
        y[i]=(b[i]-Sum)/L[i][i]

    #Backward substitution Ux= y
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        Sum=0
        for j in range(n):
            if(i!=j):
                Sum+= U[i][j]*x[j]
        x[i]=(y[i]-Sum)/U[i][i]

    print(f"Η ριζα του Αx=b ειναι: {np.array(x)}")



A=[[9,3,4],[4,3,4],[1,1,1]]

b=[7,8,3]

PALU(A,b)