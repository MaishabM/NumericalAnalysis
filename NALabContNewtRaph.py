import math

def f(x):
    return x*math.sin(x) + math.cos(x)

def df(x):
    return x*math.cos(x)

def newtonRaphson(p0,TOL,NO):
    i = 1
    if df(p0) == 0:
        print('Wrong function. Derivative cannot be zero')
        return None
    print('n     x_n      x_n+1')
    while i<=NO:
        p = p0 - (f(p0)/df(p0))
        print(f'{i}  {p0:.6f}   {p:.6f}')
        if abs(p-p0) <= TOL:
            return p
        p0 = p
        i+=1
    print('The method failed')
    return None

p0 = float(input('Enter the initial value: '))
root = newtonRaphson(p0,0.000001,30)
if root is not None:
    print(f'The root of the function is: {root:.6f}')