def newton_forward(DataX, DataY, x):
    n = len(DataX)
    h = DataX[1] - DataX[0]  # Step size
    p = (x - DataX[0]) / h  # Compute p

    # Compute forward difference table
    diff_table = [[0] * n for _ in range(n)]  # Creating an empty table
    for i in range(n):
        diff_table[i][0] = DataY[i]  # First column is y data

    for j in range(1, n):  # Compute forward differences
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]

    # Computing interpolation using Newton’s forward formula
    Result = DataY[0]
    term = 1
    for i in range(1, n):
        term *= (p - (i - 1)) / i  # Computing p terms
        Result += term * diff_table[0][i]  # Using first row of difference table

    return round(Result, 4)

# Sample Input
x_values = [1891, 1901, 1911, 1921, 1931]
y_values = [46, 66, 81, 93, 101]

FindX = 1895
y_result = newton_forward(x_values, y_values, FindX)

print(f"Interpolated value y({FindX}) = {y_result}")