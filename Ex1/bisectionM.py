import math
import time

def f(x):
    """Η συνάρτηση που εξετάζουμε."""
    return 14*x*math.exp(x-2) - 12*math.exp(x-2) - 7*x**3 + 20*x**2 - 26*x + 12

def bisection_method(a, b, tolerance):
    """
    Υλοποίηση της μεθόδου διχοτόμησης.

    Parameters:
        a (float): Αριστερό άκρο του διαστήματος.
        b (float): Δεξί άκρο του διαστήματος.
        tolerance (float): Όριο ανοχής για τη σύγκλιση.

    Returns:
        float: Η ρίζα που βρέθηκε.
        int: Πλήθος επαναλήψεων.
        bool: Επιστροφή αν υπολογίστηκε η ρίζα.
    """
    iterations = 0
    while (b - a) >= tolerance:
        middle = (a + b) / 2.0
        iterations += 1

        if f(middle) == 0.0:
            return middle, iterations, True
        elif f(middle) * f(a) < 0:
            b = middle
        else:
            a = middle

    # Επιστροφή της ρίζας και του πλήθους επαναλήψεων αν υπάρχει αποτέλεσμα
    return (a + b) / 2.0, iterations, True


def calculate_interval_roots(a, b, tolerance):
    """
    Υπολογισμός ριζών σε υποδιαστήματα με διχοτόμηση.

    Parameters:
        a (float): Αριστερό άκρο του διαστήματος.
        b (float): Δεξί άκρο του διαστήματος.
        tolerance (float): Όριο ανοχής για τη σύγκλιση.
    """
    intervals = [(a, b)]
    roots = []

    # Σπάσιμο του διαστήματος αν δεν υπάρχει αλλαγή πρόσημου
    while intervals:
        current_a, current_b = intervals.pop()
        if f(current_a) * f(current_b) > 0:
            middle = (current_a + current_b) / 2.0
            intervals.append((current_a, middle))
            intervals.append((middle, current_b))
        else:
            root, iterations, computed = bisection_method(current_a, current_b, tolerance)
            if computed:
                roots.append((root, iterations, current_a, current_b))

    return roots


# Εύρος υπολογισμών και ακρίβεια
a = 0.0
b = 3.0
tolerance = 1e-6

start = time.perf_counter()

# Υπολογισμός ριζών
roots = calculate_interval_roots(a, b, tolerance)

# Εκτύπωση αποτελεσμάτων
for root, iterations, interval_a, interval_b in roots:
    print(f"Ρίζα βρέθηκε στο διάστημα [{interval_a:.2f}, {interval_b:.2f}]: {root:.6f} μετά από {iterations} επαναλήψεις")

end = time.perf_counter()
execution_time = end - start
print(f"Συνολικός χρόνος εκτέλεσης: {execution_time:.6f} δευτερόλεπτα")