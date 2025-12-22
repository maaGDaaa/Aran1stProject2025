import math
import time

MAX_ITERATIONS = 100
TOLERANCE = 1e-6

def f(x):
    """Η συνάρτηση που εξετάζουμε."""
    return 14 * x * math.exp(x - 2) - 12 * math.exp(x - 2) - 7 * x**3 + 20 * x**2 - 26 * x + 12

def derivative_f(x):
    """Η πρώτη παράγωγος της συνάρτησης."""
    return 14 * math.exp(x - 2) + (14 * x - 12) * math.exp(x - 2) - 21 * x**2 + 40 * x - 26

def newton_raphson(x0, tolerance, max_iterations, display=False):
    """
    Υλοποίηση της μεθόδου Newton-Raphson.

    Parameters:
        x0 (float): Αρχικό σημείο.
        tolerance (float): Όριο ανοχής για τη σύγκλιση.
        max_iterations (int): Μέγιστος αριθμός επαναλήψεων.
        display (bool): Εκτύπωση ενδιάμεσων αποτελεσμάτων.

    Returns:
        float: Η ρίζα που βρέθηκε.
        int: Πλήθος επαναλήψεων.
        bool: Εάν η μέθοδος συγκλίνει.
    """
    iterations = 0
    x_current = x0

    while iterations < max_iterations:
        try:
            f_current = f(x_current)
            derivative_current = derivative_f(x_current)

            # Έλεγχος για μη μηδενική παράγωγο (αποφυγή διαιρέσεων μηδενικών)
            if abs(derivative_current) < 1e-12:
                print(f"Μηδενική παράγωγος στο x = {x_current:.6f}. Η μέθοδος απέτυχε.")
                return None, iterations, False

            # Ενημέρωση για την επόμενη τιμή x
            x_next = x_current - f_current / derivative_current
            iterations += 1

            if display:
                print(f"Eπαναληψη {iterations}: x = {x_next:.6f}, f(x) = {f_current:.6f}")

            # Έλεγχος ανοχής (σύγκλιση)
            if abs(x_next - x_current) < tolerance:
                return x_next, iterations, True

            x_current = x_next

        except ZeroDivisionError:
            print("Διαιρέση με το μηδέν. Η μέθοδος απέτυχε.")
            return None, iterations, False

    print(f"Η μέθοδος δεν συγκλίνει μετά από {max_iterations} επαναλήψεις.")
    return x_current, iterations, False


# Διαστήματα εκκίνησης
initial_points = [0.0, 1.5, 3.0]

# Υπολογισμός για κάθε αρχικό σημείο
start_time = time.perf_counter()

for x0 in initial_points:
    print(f"Έλεγχος για x0 = {x0:.2f}:")
    root, iterations, converged = newton_raphson(x0, TOLERANCE, MAX_ITERATIONS, display=True)

    if converged:
        print(f"Η μέθοδος συγκλίνει στο x = {root:.6f} μετά από {iterations} επαναλήψεις.\n")
    else:
        print(f"Η μέθοδος απέτυχε να συγκλίνει στο x0 = {x0:.2f}.\n")

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Συνολικός χρόνος εκτέλεσης: {execution_time:.6f} δευτερόλεπτα")