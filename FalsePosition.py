def f(x):
    return x**3 -2*x -5

def falsePosition(a,b,TOL,NO):
    i = 1

    if f(a)*f(b) >= 0:
        print('Invalid Interval. Two signs must be opposite')
        return None

    print('n        a           b             p                f(p)')

    while i<=NO:
        p = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
        fp = f(p)
        print(f'{i}    {a:.6f}     {b:.6f}       {p:.6f}        {fp:.6f}')

        if fp == 0 or abs(fp) <= TOL:
            return p
        elif f(a)*f(p) < 0:
            b = p
        else:
            a = p
        i+=1
    print(f'The method failed after {NO} iterations')
    return None

a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))
root = falsePosition(a,b,0.000001,25)

if root is not None:
    print(f'The root of the method is: {root:.6f}')
else:
    print('No root exists between the interval')