import math
import time

MAX = 100
tolerance = 1e-6

def f(x):
    return 14*x*math.exp(x-2) - 12*math.exp(x-2) - 7*x**3 + 20*x**2 - 26*x + 12

def secantMethod(x0, x1):
    i = 0
    while abs(f(x1)) > tolerance and i < MAX:
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_new
        i += 1

    if abs(f(x1)) <= tolerance:
        return x1,i
    else:
        print("Η μέθοδος της τέμνουσας δεν συγκλίνει εντός του καθορισμένου αριθμού επαναλήψεων")
start =   time.perf_counter()
root, iterations = secantMethod(0.0, 1.0)
root2, iterations2= secantMethod(1.5, 2.5)
end = time.perf_counter()
totalTime = end - start

print(f"Η Ριζα βρεθηκε στο x = {root:.6f} μετα απο {iterations} επαναληψεις")
print(f"Η Ριζα βρεθηκε στο x = {root2:.6f} μετα απο {iterations2} επαναληψεις")
print(f"Συνολικος χρονος : {totalTime:.6f}")