import math
def f(x):
    return math.sin(x)

def trapezoidal(a, b, n):
    h = (b - a) / n
    total = (f(a) + f(b))

    for i in range(1, n):
        x = a + i * h
        total += f(x) * 2

    return (h / 2) * total

a = 0
b = math.pi / 2

res = trapezoidal(a, b, 5)
print(f'The result is: {res:.6f}')