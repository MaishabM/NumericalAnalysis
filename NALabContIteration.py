import math

def f(x):
    return (math.cos(x) + 3) / 2

def iteration(p,TOL,NO):
    i = 1
    print('n      p       f(p)')
    while i<=NO:
        print(f'{i}  {p:.6f}   {f(p):.6f}')
        p = f(p)
        if abs(f(p)-p) <= TOL:
            return p
        i+=1
    print('The method failed')
    return None

p = float(input('Enter the initial value: '))
root = iteration(p,0.000001,30)
if root is not None:
    print(f'The root of the function is: {root:.6f}')