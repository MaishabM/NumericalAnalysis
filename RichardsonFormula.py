import math

def f(x):
    return math.log(x)

def central(f,x,h):
    return (f(x+h)-f(x-h)) / (2*h)

def richardson(f,x,n):
    N = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        h = 1/ 2**(i+1)
        N[i][0] = central(f,x,h)

    for k in range(1,n):
        for i in range(n-k):
            N[i][k] = (2**k * N[i+1][k-1] - N[i][k-1]) / (2**k - 1)

    for i in range(n):
        for j in range(n):
            print(f'{N[i][j]:<8.6f}',end='  ')
        print()

    return N[0][k-1]

x = float(input('Enter the value: '))
n = int(input('Enter number of iteration: '))
approx = richardson(f,x,n)
print(f'The approximate value of the derivative of the equation: {approx:.6f}')