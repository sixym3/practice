import sympy
import numpy as np

# Modify these to find the roots of the given cubic polynomial
x = sympy.symbols('x')
roots = sympy.roots(816*x**3 - 3835*x**2 + 6000*x - 3125)
print(roots)
xroots = [sympy.N(r) for r in roots]  # Compute the numerical values
print(xroots)

print(np.roots([-1.0, -1.0, 12.0]))
