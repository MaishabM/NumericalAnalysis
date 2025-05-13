n = 5
x = [1.0, 1.3, 1.6, 1.9, 2.2]
y=[[0 for i in range(n)]for j in range(n)]

y[0][0] = 0.7651977
y[1][0] = 0.6200860
y[2][0] = 0.4554022
y[3][0] = 0.2818186
y[4][0] = 0.1103623

for col in range(1,n):
    for row in range(n-col):
        y[row][col] = (y[row+1][col-1] - y[row][col-1]) / (x[row+col]-x[row])

print('Divided Difference table: ')
for i in range(n):
    print(f'{x[i]}',end = '  ')
    for j in range(n-i):
        print(f'{y[i][j]:.6f}',end= '  ')
    print()

product = 1
res = y[0][0]
value = float(input('Enter the value: '))

for i in range(1,n):
        product *= (value- x[i-1])
        res += (product * y[0][i])

print(f'The interpolated value at {value} is: {res:.6f}')