import math
def f(x):
    return math.sin(x)

def simpson(lower,upper,n):
    h = (upper - lower)/n
    total = f(lower) + f(upper)

    for i in range(1,n):
        x = lower + (i*h)
        if i%2==0:
            total += 2 * f(x)
        else:
            total += 4*f(x)
    return total * (h/3)

l = float(input('Enter the lower limit: '))
u = float(input('Enter the upper limit: '))
res = simpson(l,u,5)
print(f'The result: {res:.6f}')