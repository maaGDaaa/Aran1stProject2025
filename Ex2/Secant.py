import math
import time

MAX_ITERATIONS = 100
TOLERANCE = 1e-6

def f(x):
    """Η συνάρτηση f(x)."""
    return 54*(x**6) + 45*(x**5) - 102*(x**4) - 69*(x**3) + 35*(x**2) + 16*x - 4

def modified_secant_method(x0, x1, x2, tolerance, max_iterations):
    """
    Τροποποιημένη μέθοδος τέμνουσας με χρήση τριών σημείων.
    """
    root = [x0, x1, x2]
    iterations = 0
    start_time = time.perf_counter()

    while iterations < max_iterations:
        try:
            q = f(root[iterations]) / f(root[iterations + 1])
            r = f(root[iterations + 2]) / f(root[iterations + 1])
            s = f(root[iterations + 2]) / f(root[iterations])
            numerator = r * (r - q) * (root[iterations + 2] - root[iterations + 1]) + (1 - r) * s * (root[iterations + 2] - root[iterations])
            denominator = (q - 1) * (r - 1) * (s - 1)

            if abs(denominator) > 1e-12:
                new_root = root[iterations + 2] - (numerator / denominator)
                root.append(new_root)

                if abs(root[iterations + 3] - root[iterations + 2]) < tolerance:
                    end_time = time.perf_counter()
                    total_time = end_time - start_time
                    print(f"Ρίζα: {root[iterations + 3]:.6f}, Επαναλήψεις: {iterations + 1}, Συνολικός χρόνος: {total_time:.6f} δευτερόλεπτα")
                    return root[iterations + 3], iterations + 1, total_time

            iterations += 1
        except ZeroDivisionError:
            print("Διαιρέση με το μηδέν, η μέθοδος απέτυχε.")
            return None, iterations, None

    print("Η μέθοδος απέτυχε να συγκλίνει.")
    return None, iterations, None


# Εκτελέσεις για δεδομένα αρχικά σημεία:
initial_guesses = [(-2.0, -1.9, -1.8), (-1.0, -0.9, -0.8), (0.0, 0.1, 0.2), (0.6, 0.7, 0.8), (1.0, 1.1, 1.2)]

print("-----------------------------")
for x0, x1, x2 in initial_guesses:
    print(f"Αρχικά σημεία: {x0:.1f}, {x1:.1f}, {x2:.1f}")
    modified_secant_method(x0, x1, x2, TOLERANCE, MAX_ITERATIONS)