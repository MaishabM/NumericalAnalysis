def product(p,n):
    pro = 1
    for i in range(n):
        pro *= (p+i)

    return pro

def fact(n):
    if n<=1:
        return 1

    return n* fact(n-1)

n = 5
value = float(input('Enter the interpolation point: '))
x = [1891,1901,1911,1921,1931]
y = [[0 for i in range(n)] for j in range(n)]
y[0][0] = 46
y[1][0] = 66
y[2][0] = 81
y[3][0] = 93
y[4][0] = 101

for i in range(1,n):
    for j in range(n-1,i-1,-1):
        y[j][i] = y[j][i-1] - y[j-1][i-1]

print('Backward Difference Table: ')
for i in range(n):
    print(f'{x[i]}',end = '  ')
    for j in range(i+1):
        print(f'{y[i][j]}',end= '  ')
    print()

res = y[n-1][0]
p = (value - x[n-1]) / (x[1]- x[0])

for i in range(1,n):
    res += (product(p,i) * y[n-1][i]) / fact(i)

print(f'The interpolated value at {value} is: {res:.6f}')