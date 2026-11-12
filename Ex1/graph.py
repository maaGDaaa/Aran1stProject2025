import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 14 * x * np.exp(x - 2) - 12 * np.exp(x - 2) - 7 * x**3 + 20 * x**2 - 26 * x + 12

x = np.linspace(0, 3, 1000)
y = f(x)

plt.plot(x, y, label="f(x)")
plt.axhline(0, color='red', linestyle='--', label="y = 0")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Γραφική παράσταση της συνάρτησης f(x)")
plt.legend()
plt.show()