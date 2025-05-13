import math

def trapezoidal(f, a, b, n):
    h = (b - a) / n
    total = (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * h
        total += f(x)
    return h * total

# Example: ∫₀^{π/2} sin(x) dx
f = lambda x: math.sin(x)
result = trapezoidal(f, 0, math.pi/2, 4)
print(f"Approximate integral: {result:.10f}")