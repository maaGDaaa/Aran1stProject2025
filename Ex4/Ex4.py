import numpy as np

n= 15
q = 0.15


# Αρχικοποιηση του πινακα Α
A = np.zeros((n,n))
A[0][1]=1
A[0][8]=1
A[1][2]=1
A[1][4]=1
A[1][6]=1
A[2][1]=1
A[2][5]=1
A[2][7]=1
A[3][2]=1
A[3][11]=1
A[4][0]=1
A[4][9]=1
A[5][9]=1
A[5][10]=1
A[6][9]=1
A[6][10]=1
A[7][3]=1
A[7][10]=1
A[8][4]=1
A[8][5]=1
A[8][9]=1
A[9][12]=1
A[10][14]=1
A[11][6]=1
A[11][7]=1
A[11][10]=1
A[12][8]=1
A[12][13]=1
A[13][9]=1
A[13][10]=1
A[13][12]=1
A[13][14]=1
A[14][11]=1
A[14][13]=1

#  Ερωτημα 4.1

def denominator(A,i):
    n = len(A)
    sum=0
    for j in range(n):
        sum=sum+A[i][j]
    return sum

def calc_G(A,q):
    n = len(A)
    G = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            G[i][j]=q/n + (A[j][i]*(1-q)/denominator(A,j))
    return G

G=calc_G(A,q)
col_sum = np.zeros(n)
for j in range(n):
    sum=0
    for i in range(n):
        sum=sum+G[i][j]
    col_sum[j] = sum

print("Υποερωτημα 1.\n")
print(col_sum)
print("Αφου ολες οι στηλες εχουν αθροισμα 1 τοτε ο G ειναι στοχαστικος")


# Ερωτημα 4.2
print("----------------------------------------------")
print("Υποερωτημα 2.\n")

def powerMethod(G,n):
    # Τυχαιο διανυσμα x . Το αναλυω σε συνιστωσες x1, x2
    x0 = np.zeros(n)
    x1 = np.zeros(n)

    # Αρχικοποιω το πρωτο διανυσμα με την πρωτη στηλη του Α
    for i in range(n):
        x0[i]=G[i][0]

    for i in range(n):
        for j in range(n):
            x1[i]+= G[i][j]*x0[j]
    old_l=x1[0]
    for i in range(n):
        x1[i]=x1[i]/old_l


    l=100
    while(abs(old_l-l)>0.0001):
        old_l=l
        x0=x1
        x1=np.zeros(n)
        for i in range(n):
            for j in range(n):
                x1[i]=x1[i]+G[i][j]*x0[j]
        l=x1[0]
        for i in range(n):
            x1[i]=x1[i]/l

    #Κανονικοποιηση
    sum=0
    print("p= [", end='')
    for i in range(n):
        sum=sum+x1[i]
    for i in range(n):
        normalizedVector = x1[i]/sum
        print(f"{normalizedVector:.7f}" ,end= ' ')
    print("]")
powerMethod(G,15)


# Ερωτημα 4.3
oldA = np.copy(A)
oldG = calc_G(oldA,q)


A[11][14]=1 # 12 -> 15
A[7][14]=1 # 8 ->15
A[14][10]=1 # 15-> 11
A[9][14]=1 # 10 -> 15
A[14][13]=0 # 15 -> 14

newG= calc_G(A, q)
old = 0
new = 0
for i in range(n):
    old += oldG[14][i]
    new += newG[14][i]

print("----------------------------------------------")
print("Υποερωτημα 3.\n")
print(f"Παλια σημαντικοτητα σελιδας 15 : {old}")
print(f"Νεα σημαντικοτητα σελιδας 15 : {new}")



# Ερωτημα 4.4
print("----------------------------------------------")
print("Υποερωτημα 4.\n")

q0 = 0.02
q1 = 0.6
G0 = calc_G(A,q0)
G1 = calc_G(A,q1)
sum1 = np.zeros(n)
sum2 = np.zeros(n)

powerMethod(G0,15)
print("\n")
powerMethod(G1,15)



# Ερωτημα 4.5
print("----------------------------------------------")
print("Υποερωτημα 5.\n")

G = calc_G(oldA,q)
powerMethod(G,15)


oldA[7][10]=3
oldA[11][10]=3
G = calc_G(oldA,q)
powerMethod(G,15)


# Ερωτημα 4.6
print("----------------------------------------------")
print("Υποερωτημα 6.\n")

oldA[7][10]=1
oldA[11][10]=1

G = calc_G(oldA,q)
powerMethod(G,15)


oldA = np.delete(oldA,9,axis= 0)
oldA = np.delete(oldA,9,axis= 1)



G = calc_G(oldA,q)
powerMethod(G,14)
