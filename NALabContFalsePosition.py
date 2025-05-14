import math

def f(x):
    return math.exp(x) + 2 ** (-x) + 2*math.cos(x) - 6

def falsePosition(a,b,TOL,NO):
    i = 1
    if f(a)*f(b) > 0:
        print('Wrong interval')
        return None

    print('n       a           b           p         f(p)')
    while i<=NO:
        p = (a*f(b) - b*f(a)) / (f(b) - f(a))
        print(f'{i}   {a:.6f}    {b:.6f}    {p:.6f}   {f(p):.6f}')
        if f(p) == 0 or abs(f(p)) <= TOL:
            return p
        elif f(a)*f(p) < 0:
            b = p
        else:
            a = p
        i+=1
    print('The method failed')
    return None

a = float(input('Enter the first interval: '))
b = float(input('Enter the second interval: '))

root = falsePosition(a,b,0.000001,30)
if root is not None:
    print(f'The root of the function is: {root:.6f}')