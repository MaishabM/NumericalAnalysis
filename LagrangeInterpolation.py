n = 4
x = [1,3,5,7]
y = [24,120,336,720]
value = float(input('Enter the value: '))

total = 0.0

for i in range(n):
    res = y[i]
    for j in range(n):
        if i!=j:
            res *=  (value - x[j]) / (x[i] - x[j])
    total += res

print(f'The interpolation at {value} is: {total:.6f}')