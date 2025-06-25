import math

n = 3
x = [0, math.pi/4 ,math.pi/2]
y = [0, 0.70711, 1.0]
value = math.pi / 6

total = 0.0
for i in range(n):
    l = y[i]
    for j in range(n):
        if i != j:
            l *= (value-x[j]) / (x[i]-x[j])
    total += l
print(f'The interpolated result at sin(pi/6) is: {total:.6f}')