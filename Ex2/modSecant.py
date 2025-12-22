import time

MAX = 100
tol = 1e-7

def f(x):
    return 54*(x**6) + 45*(x**5) -102*(x**4) -69*(x**3) +35*(x**2) +16*x-4

def mod_Secant(a,b,c):
    start = time.perf_counter()
    i = 0
    found = False
    root = [a,b,c]

    while not found:
        q = f(root[i]) / f(root[i+1])
        r = f(root[i+2]) / f(root[i+1])
        s = f(root[i+2]) / f(root[i])

        numerator = r* (r-q)* (root[i+2]-root[i+1]) + (1-r)*s *(root[i+2]-root[i])
        denomirator = (q-1) * (r-1) * (s-1)

        if denomirator != 0 :
            root.append(root[i+2] - (numerator/denomirator))

        if abs(root[i+3]-root[i+2]) < tol /2 :
            found = True

        if i> MAX :
            break
        i+= 1

    end = time.perf_counter()
    totalTime = end - start
    print("---------------------------------------")
    print(f"Η ριζα ειναι {root[i]:.7f} και βρεθηκε μετα απο {i} επαναληψεις")
    print(f"Συνολικος χρονος: {totalTime:.6f}")


mod_Secant(-2.0,-1.9,-1.8)
mod_Secant(-1.0,-0.9,-0.8)
mod_Secant(0.0,0.1,0.2)
mod_Secant(0.6,0.7,0.8)
mod_Secant(1.0,1.1,1.2)
