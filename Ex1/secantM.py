import math
import time

MAX_ITERATIONS = 100
TOLERANCE = 1e-6

def f(x):
    """Η συνάρτηση που εξετάζουμε."""
    return 14*x*math.exp(x-2) - 12*math.exp(x-2) - 7*x**3 + 20*x**2 - 26*x + 12

def secant_method(x0, x1, tolerance, max_iterations):
    """
    Υλοποίηση της μεθόδου τέμνουσας.

    Parameters:
        x0 (float): Πρώτο αρχικό σημείο.
        x1 (float): Δεύτερο αρχικό σημείο.
        tolerance (float): Όριο ανοχής για τη σύγκλιση.
        max_iterations (int): Μέγιστος αριθμός επαναλήψεων.

    Returns:
        float: Η ρίζα που βρέθηκε.
        int: Πλήθος επαναλήψεων.
        bool: Εάν η μέθοδος συγκλίνει.
    """
    iterations = 0
    while iterations < max_iterations:
        try:
            # Υπολογισμός νέας προσέγγισης χρησιμοποιώντας τη μέθοδο τέμνουσας
            if abs(f(x1) - f(x0)) < 1e-12:
                print(f"Διαιρέση με πολύ μικρή τιμή στο x0 = {x0:.6f} και x1 = {x1:.6f}. Η μέθοδος απέτυχε.")
                return None, iterations, False

            x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
            iterations += 1

            if abs(x_new - x1) < tolerance:
                return x_new, iterations, True

            # Ενημέρωση για την επόμενη επανάληψη
            x0, x1 = x1, x_new

        except ZeroDivisionError:
            print("Διαιρέση με το μηδέν. Η μέθοδος απέτυχε.")
            return None, iterations, False

    print(f"Η μέθοδος δεν συγκλίνει μετά από {max_iterations} επαναλήψεις.")
    return x1, iterations, False


# Διαστήματα εκκίνησης
intervals = [(0.0, 1.0), (1.5, 2.5), (2.5, 3.0)]

# Επαναληπτικοί υπολογισμοί για καθένα από τα διαστήματα
start_time = time.perf_counter()

for x0, x1 in intervals:
    print(f"Έλεγχος για x0 = {x0:.2f}, x1 = {x1:.2f}:")
    timings = []

    for _ in range(10):  # Εκτέλεση 10 φορές για σύγκριση
        start = time.perf_counter()

        root, iterations, converged = secant_method(x0, x1, TOLERANCE, MAX_ITERATIONS)

        end = time.perf_counter()
        timings.append(end - start)

        if converged:
            print(f"Η μέθοδος συγκλίνει στο x = {root:.6f} μετά από {iterations} επαναλήψεις.")
        else:
            print(f"Η μέθοδος απέτυχε για το διάστημα [{x0:.2f}, {x1:.2f}].")

    print(f"Μέσος χρόνος εκτέλεσης για το διάστημα [{x0:.2f}, {x1:.2f}]: {sum(timings) / len(timings):.6f} δευτερόλεπτα.\n")

end_time = time.perf_counter()
total_execution_time = end_time - start_time
print(f"Συνολικός χρόνος εκτέλεσης: {total_execution_time:.6f} δευτερόλεπτα.")