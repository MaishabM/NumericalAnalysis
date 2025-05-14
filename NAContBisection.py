def f(x):
    return x**3 - 2*x -5

def bisection(a,b,TOL,NO):
    i = 1
    if f(a)*f(b) > 0:
        print('Wrong intervals')
        return None
    print('n      a         b           p           f(p)')
    while i<= NO:
        p = (a+b)/2
        print(f'{i}  {a:.6f}   {b:.6f}    {p:.6f}   {f(p):.6f}')

        if f(p)==0 or (b-a)/2 <= TOL:
            return p
        elif f(p)*f(a) < 0:
            b = p
        else:
            a = p
        i += 1
    print('Method failed')
    return None

a = float(input('Enter the first interval: '))
b = float(input('Enter the second interval: '))

root = bisection(a,b,0.000001,30)
if root is not None:
    print(f'The root of the function is: {root:.6f}')