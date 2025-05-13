import math


# Centered finite difference approximation
def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


# Richardson Extrapolation for first derivative
def richardson_derivative(f, x, n=10):
    N = [[0.0 for i in range(n)] for j in range(n)]

    # Fill first column with approximations using smaller and smaller h
    for i in range(n):
        h = 1 / (2 ** (i + 1))
        N[i][0] = central_difference(f, x, h)

    # Richardson extrapolation to refine estimates
    for k in range(1, n):
        for i in range(n - k):
            N[i][k] = (2 ** k * N[i + 1][k - 1] - N[i][k - 1]) / (2 ** k - 1)

    return N[0][n - 1]


# Example: derivative of ln(x) at x = 1.8
f = lambda x: math.log(x)
x0 = 1.8

approx = richardson_derivative(f, x0)
exact = 1 / x0

print(f"Approximate derivative at x = {x0}: {approx:.15f}")
print(f"Exact derivative (1/x) at x = {x0}: {exact:.15f}")