def iteration(p,TOL,NO):
    i = 1
    print('n    p     g(p)')
    while i<=NO:
        p = g(p)
        print(f'{i}  {p:.6f}  {g(p):.6f}')
        if abs(g(p) - p) <= TOL:
            return p
        i += 1
    print('Method failed')
    return None

g = lambda x: 1 / ((x + 1) ** (1/2))
p0 = float(input('Enter initial value: '))

root = iteration(p0,0.000001,30)
if root is not None:
    print(f'The root of the function is: {root:.6f}')