import time

MAX = 100
tol = 1e-7

def f(x):
    return 54*(x**6) + 45*(x**5) -102*(x**4) -69*(x**3) +35*(x**2) +16*x-4

def derivative1_f(x):
    return 324*x**5 + 225*x**4 - 408*x**3 - 207*x**2 + 70*x + 16

def derivative2_f(x):
    return 1620*x**4 + 900*x**3 - 1224*x**2 - 414*x +70

def mod_Newton(init):
    start = time.perf_counter()
    i=0
    x0 = init
    found = False
    print("-----------------------------")

    while not found:
        x1 = x0 - 1.0 /((derivative1_f(x0) / f(x0)) - (derivative2_f(x0) / (2.0 * derivative1_f(x0))))
        if abs(x1 - x0) < tol / 2 :
            found = True
        x0 = x1
        i+= 1

    if found :
        print("Η ριζα ειναι: {:.7f} μετα απο {} επαναληψεις".format(x0, i))
    else:
        print("Δεν βρεθηκε ριζα")

    end = time.perf_counter()
    total_time = end - start
    print("Συνολικος Χρονος: {:.6f}".format(total_time))

mod_Newton(-2.0)
mod_Newton(-1.0)
mod_Newton(0.0)
mod_Newton(0.3)
mod_Newton(1.1)