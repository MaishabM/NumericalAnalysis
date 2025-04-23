import math


def D(Func, a, h):
    '''Centered finite difference method to calculate the derivative at x=a'''
    return (Func(a + h) - Func(a - h)) / (2 * h)


def Richardson_dif(func, a, max_order=10):
    '''Richardson extrapolation for numerical derivative.
       It computes higher order derivatives using the basic central difference method.
    '''
    # Initialize an array for approximations
    N = [[0 for _ in range(max_order)] for _ in range(max_order)]

    # Calculate initial approximations for different step sizes
    for I in range(max_order):
        N[I][0] = D(func, a, 1 / (2 ** (I + 1)))

    # Richardson extrapolation for higher orders
    for k in range(1, max_order):
        for i in range(max_order - k):
            N[i][k] = ((2 ** (k)) * N[i + 1][k - 1] - N[i][k - 1]) / (2 ** (k) - 1)

    return N[0][max_order - 1]


# Example usage: First derivative of ln(x) at x = 1.8
f = lambda x: math.log(x)
result = Richardson_dif(f, 1.8)
print(f"First derivative of ln(x) at x = 1.8 is approximately: {result:.15f}")
print(f"The exact value of ln(x) at x = 1.8 is: {math.log(1.8):.15f}")

# Example usage: Higher-order derivatives (e.g., 2nd derivative) can be approximated similarly
# Just change the `max_order` and adjust the function accordingly.