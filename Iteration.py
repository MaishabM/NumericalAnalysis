import math

def f(x):
    return (math.cos(x) + 3)/2

def iteration(p0,TOL,NO):
    i = 1
    print('n     p         f(p)')

    while i<=NO:
        p = f(p0)
        print(f'{i}  {p0:<10.6f}  {p:<10.6f}')

        if abs(p-p0) <= TOL:
            return p
        p0 = p
        i+=1
    print(f'The method failed after {NO} iterations')
    return None

p = float(input('Enter the initial value: '))
root = iteration(p,0.000001,30)
if root is not None:
    print(f'The root of the equation is: {root:.6f}')