import math
import time

MAX = 100
tol = 1e-6
Print = False

def f(x):
    return 14*x*math.exp(x-2) - 12*math.exp(x-2) - 7*x**3 + 20*x**2 - 26*x + 12

def derivative1_f(x):
    return 14 * x * math.exp(x - 2) + 2 * math.exp(x - 2) - 21 * x**2 + 40 * x - 26


def newtonRaphson(x0,Print):
    found = False
    i=0

    while True:
        x1 = x0 - f(x0) / derivative1_f(x0)
        if abs(x1 - x0) < tol/2:
            found = True
            break
        if Print:
            print(f"x1: {x1:.5f}, Sqare: {(x1**2):.5f}")
        x0 = x1
        i += 1
        if i >= MAX:
            found = True
            break

    if found:
        print(f"Η διαδικασία ολοκληρώθηκε με {i} επαναληψεις.\nΗ ριζα ειναι: {x0:.6f}")
    else:
        print(f"Η μεθοδος απετυχε μετα απο {i} επαναληψεις.")

start = time.perf_counter()
newtonRaphson(0.0,False)
newtonRaphson(3.0,False)
end = time.perf_counter()
totalTime = end -start
print(f"Συνολικος χρονος : {totalTime:.6f}")