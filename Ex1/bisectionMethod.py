import math
import time

def f (x):
    return 14*x*math.exp(x-2) - 12*math.exp(x-2) - 7*x**3 + 20*x**2 - 26*x + 12

def biseciton_method(x,y,lim):
    mid = 0
    times = 0

    while (y-x) >= lim:
        mid = (x+y)/2.0
        times += 1

        if f(mid)== 0.0:
            break
        elif f(mid)*f(x) <0 :
            y=mid
        else:
            x=mid
    return mid , times

x=0.0
y=3.0
limit = 1e-6
mid = 1.5

if f(x) * f(y) > 0:
    print("Η μεθοδος της διχοτομησης δεν μπορει να υλοποιηθει στο συγκεκριμενο διαστημα! Χρειαζεται διασπαση του διαστηματος")


start = time.perf_counter()
new_value, times = biseciton_method(x, mid, limit)
print(f"Η συγκλινουσα ριζα στο διαστημα [0,1] ειναι: {new_value:.6f} και βρεθηκε μετα απο {times} επαναληψεις")

new_value, times = biseciton_method(mid, y, limit)
print(f"Η συγκλινουσα ριζα στο διαστημα [1.5,3] ειναι: {new_value:.6f} και βρεθηκε μετα απο {times} επαναληψεις")

end = time.perf_counter()

totalTime = end - start
print(f"Συνολικος Χρονος εκτελεσης: {totalTime:.6f}")






