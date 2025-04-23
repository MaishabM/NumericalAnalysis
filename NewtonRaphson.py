def f(x):
    return x ** 3 - 2 * x - 5


def df(x):
    return 3 * x ** 2 - 2


def newtonRaphson(p0, TOL, NO):
    i = 1
    print('n      x_n        x_n+1')

    while i <= NO:
        fp0 = f(p0)
        dfp0 = df(p0)

        if dfp0 == 0:
            print('The derivative is 0. Invalid function')
            return None

        p = p0 - (fp0 / dfp0)
        print(f'{i}    {p0:.6f}    {p:.6f}')

        if abs(p - p0) <= TOL:
            return p
        p0 = p
        i += 1

    print('The method failed after {NO} iterations')
    return None


a = float(input('Enter the value of p: '))
root = newtonRaphson(a, 0.0000001, 10)

if root is not None:
    print(f'The root of the function is: {root:.6f}')
else:
    print('No root exists')