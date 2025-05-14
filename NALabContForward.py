def product(p,n):
    pro = 1
    for i in range(n):
        pro *= (p-i)
    return pro

def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

n = 4
x = [0,1,2,3]
y = [[0 for i in range(n)]for j in range(n)]
value = float(input('Enter the interpolation point: '))
y[0][0] = -1
y[1][0] = 1
y[2][0] = 7
y[3][0] = 25

for j in range(1,n):
    for i in range(n-j):
        y[i][j] = y[i+1][j-1] - y[i][j-1]

print('The forward difference table: ')
for i in range(n):
    print(f'{x[i]}',end='  ')
    for j in range(n):
        if j <= n-i-1:
            print(f'{y[i][j]}',end='  ')
    print()

p = (value - x[0]) / (x[1]-x[0])
res = y[0][0]
for i in range(1,n):
    res += (product(p,i) * y[0][i]) / fact(i)
print(f'The interpolated result at y({value}): {res:.6f}')