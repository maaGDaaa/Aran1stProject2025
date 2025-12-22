import math
import time


MAX_ITERATIONS = 20
TOLERANCE = 1e-6

def f(x):
    """Η συνάρτηση f(x)."""
    return 54*(x**6) + 45*(x**5) - 102*(x**4) - 69*(x**3) + 35*(x**2) + 16*x - 4


def modified_bisection(a, b, tolerance, max_iterations):
    """
    Τροποποιημένη μέθοδος διχοτόμησης με έλεγχο κατάλληλου διαστήματος.
    """
    iterations = 0
    start_time = time.perf_counter()

    # Έλεγχος αλλαγής πρόσημου στο αρχικό διάστημα
    if f(a) * f(b) > 0:
        print(f"Το διάστημα [{a:.2f}, {b:.2f}] δεν περιέχει ρίζα (δεν υπάρχει αλλαγή πρόσημου).")
        return None, iterations, None

    while iterations < max_iterations and (b - a) >= tolerance:
        # Υπολογισμός σημείου στο 1/3 του διαστήματος προς το κοντινότερο άκρο
        if abs(f(a)) < abs(f(b)):
            middle = a + (b - a) / 3.0
        else:
            middle = b - (b - a) / 3.0

        iterations += 1

        # Έλεγχος σύγκλισης
        if abs(f(middle)) < tolerance:
            end_time = time.perf_counter()
            total_time = end_time - start_time
            print(f"Ρίζα: {middle:.6f}, Επαναλήψεις: {iterations}, Συνολικός χρόνος: {total_time:.6f} δευτερόλεπτα")
            return middle, iterations, total_time

        # Ενημέρωση διαστήματος βάσει αλλαγής πρόσημου
        if f(a) * f(middle) < 0:
            b = middle
        else:
            a = middle

    # Αν η μέθοδος δεν φτάσει στην απαιτούμενη ανοχή
    print(f"Η μέθοδος απέτυχε να συγκλίνει στο διάστημα [{a:.2f}, {b:.2f}].")
    return None, iterations, None


# Εκτελέσεις για δεδομένα διαστήματα:
intervals = [(-2.0, -1.0), (0.0, 0.4), (0.4, 1.0), (1.0, 2.0)]

print("-----------------------------")
for a, b in intervals:
    print(f"Διάστημα: [{a:.1f}, {b:.1f}]")
    modified_bisection(a, b, TOLERANCE, MAX_ITERATIONS)