import math

def f(x):
    return math.log(x)

n = 3
h = 0.5
x = [0 for _ in range(n)]
y = [0 for _ in range(n)]

for i in range(n):
    x[i] = 2 + i*h
    y[i] = f(x[i])

value = float(input('Enter the value: '))

print('x:')
for i in range(n):
    print(f'{x[i]}',end='  ')
print('\ny:')
for i in range(n):
    print(f'{y[i]:.5f}',end='  ')

total = 0.0

for i in range(n):
    res = y[i]
    for j in range(n):
        if i!=j:
            res *=  (value - x[j]) / (x[i] - x[j])
    total += res

print(f'\nThe interpolation at {value} is: {total:.6f}')