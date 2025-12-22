import numpy as np

def lu_decomposition_with_pivoting(A):

    n = len(A)
    A = np.array(A, dtype=float)
    P = np.eye(n)
    L = np.zeros((n, n))
    U = np.array(A)

    for i in range(n):
        # Pivoting
        max_row = np.argmax(abs(U[i:, i])) + i
        if i != max_row:
            U[[i, max_row], :] = U[[max_row, i], :]
            P[[i, max_row], :] = P[[max_row, i], :]
            if i > 0:
                L[[i, max_row], :i] = L[[max_row, i], :i]

        for j in range(i + 1, n):
            L[j, i] = U[j, i] / U[i, i]
            U[j, i:] -= L[j, i] * U[i, i:]

    np.fill_diagonal(L, 1)
    return P, L, U

def solve_lu(P, L, U, b):
    Pb = np.dot(P, b)

    n = len(L)
    y = np.zeros(n)
    for i in range(n):
        y[i] = Pb[i] - np.dot(L[i, :i], y[:i])

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x

# Example usage:
A = [[2, -1, 1],
     [3, 3, 9],
     [3, 3, 5]]

b = [2, 0, 6]

P, L, U = lu_decomposition_with_pivoting(A)
print("P =\n", P)
print("L =\n", L)
print("U =\n", U)

x = solve_lu(P, L, U, b)
print("Solution x =", x)