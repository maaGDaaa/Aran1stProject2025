import time

MAX_REPS = 20
tol = 1e-7

def func(x):
    return 54*(x**6) + 45*(x**5) -102*(x**4) -69*(x**3) +35*(x**2) +16*x-4

def mod_Bisection(x, y, lim):
    i = 0
    while y - x >= lim and i != MAX_REPS:
        i += 1
        third_interval = (y - x) / 3
        candidate_x = x + third_interval
        candidate_y = y - third_interval

        if abs(func(candidate_x)) < abs(func(candidate_y)):
            estimated_root = candidate_x
        else:
            estimated_root = candidate_y

        if abs(func(estimated_root)) >= lim:
            if func(estimated_root) * func(x) < 0:
                y = estimated_root
            else:
                x = estimated_root
        else:
            break

    return estimated_root, i

def printFunction(a, b, tol):
    print("----------------------------")
    start = time.perf_counter()
    newValue, times = mod_Bisection(a, b, tol)
    end = time.perf_counter()
    totalTime = end - start
    print(f"Η ριζα ειναι {newValue:.7f} και βρεθηκε μετα απο {times} επαναληψεις")
    print(f"Συνολικος Χρονος : {totalTime:.6f}.")


printFunction(-2.0, -1.0, tol)
printFunction(0.0, 0.4, tol)
printFunction(0.4, 1.0, tol)
printFunction(1.0, 2.0, tol)