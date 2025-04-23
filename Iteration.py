def iteration(f,p,TOL,NO):
    i = 1
    print("n            p             f(p) ")

    while i <= NO:
        print(f'{i}         {p:.6f}       {f(p):.6f}')
        if abs(f(p) - p) <= TOL:
            return p

        p = f(p)
        i += 1

    print('The method failed.')
    return None

#g1 = lambda x: (1- x**2) ** (1/3)
#g2 = lambda x: (1- x**3) ** (1/2)
g3 = lambda x: 1 / ((x + 1) ** (1/2))

#iteration(g1,0.5,0.000001,30)
#iteration(g2,0.5,0.000001,30)
root = iteration(g3,0.5,0.000001,30)

if root is not None:
    print(f'The root of the method is: {root:.6f}')
else:
    print('No root exists')