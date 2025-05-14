import math

def f(x):
    return 1/(1+x**2)

def simpson(a,b,n):
    h = (b-a) / n
    total = f(a)+f(b)
    for i in range(1,n):
        x = a + i*h
        if i%3 == 0:
            total += 2*f(x)
        else:
            total += 3*f(x)
    return total * ((3*h)/8)

a = float(input('Enter the lower limit: '))
b = float(input('Enter the upper limit: '))

res = simpson(a,b,6)
print(f'The result: {res:.6f}')