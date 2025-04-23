import math

def f(x):
    return x*math.exp(x)

h = 0.2
x0 = 2.0

res = (-3*f(x0) + 4*f(x0+h) - f(x0+2*h)) / (2*h)
print(f'The three point endpoint formula: {res:.5f}')


res = (f(x0+h) - f(x0-h)) / (2*h)
print(f'The three point midpoint formula: {res:.5f}')