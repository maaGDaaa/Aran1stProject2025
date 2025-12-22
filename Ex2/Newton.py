import math
import time

MAX_ITERATIONS = 100
TOLERANCE = 1e-6

def f(x):
    """Η συνάρτηση f(x)."""
    return 54*(x**6) + 45*(x**5) - 102*(x**4) - 69*(x**3) + 35*(x**2) + 16*x - 4

def derivative1_f(x):
    """Η πρώτη παράγωγος της συνάρτησης."""
    return 324*x**5 + 225*x**4 - 408*x**3 - 207*x**2 + 70*x + 16

def derivative2_f(x):
    """Η δεύτερη παράγωγος της συνάρτησης."""
    return 1620*x**4 + 900*x**3 - 1224*x**2 - 414*x + 70

def modified_newton_raphson(x0, tolerance, max_iterations):
    """
    Τροποποιημένη μέθοδος Newton-Raphson.
    """
    iterations = 0
    start_time = time.perf_counter()

    while iterations < max_iterations:
        try:
            # Υπολογισμός της νέας προσέγγισης
            x1 = x0 - 1.0 / ((derivative1_f(x0) / f(x0)) - (derivative2_f(x0) / (2.0 * derivative1_f(x0))))
            iterations += 1

            # Έλεγχος σύγκλισης
            if abs(x1 - x0) < tolerance:
                end_time = time.perf_counter()
                total_time = end_time - start_time
                print(f"Ρίζα: {x1:.6f}, Επαναλήψεις: {iterations}, Συνολικός χρόνος: {total_time:.6f} δευτερόλεπτα")
                return x1, iterations, total_time

            x0 = x1
        except ZeroDivisionError:
            print("Η μέθοδος απέτυχε λόγω διαιρέσεως με το μηδέν.")
            return None, iterations, None

    print("Η μέθοδος απέτυχε να συγκλίνει.")
    return None, iterations, None


# Εκτελέσεις για δεδομένα αρχικά σημεία:
initial_points = [-2.0, -1.0, 0.0, 0.4, 1.0]

print("-----------------------------")
for x0 in initial_points:
    print(f"Αρχικό σημείο: {x0:.1f}")
    modified_newton_raphson(x0, TOLERANCE, MAX_ITERATIONS)