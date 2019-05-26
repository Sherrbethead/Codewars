'''Description

Consider the sequence U(n, x) = x + 2x**2 + 3x**3 + .. + nx**n where x is a real number and n a positive integer.
When n goes to infinity and x has a correct value (ie x is in its domain of convergence D), U(n, x) goes to a finite
limit m depending on x.
Usually given x we try to find m. Here we will try to find x (x real, 0 < x < 1) when m is given (m real, m > 0).
Let us call solve the function solve(m) which returns x such as U(n, x) goes to m when n goes to infinity.
Note:
You pass the tests if abs(actual - expected) <= 1e-12.'''


def solve(m):
    '''U = x + 2*x^2 + 3*x^3 + ... + n*x^n
    x*U = x^2 + 2*x^3 + 3*x^4 + ... + (n - 1)*x^n + n*x^(n + 1)
    (1 - x)*U = x + x^2 + x^3 + ... + x^n - n*x^(n + 1)
                x*(1 - x^n)
    (1 - x)*U = -----------  -  n*x^(n + 1)
                   1-x
        x*(1 - x^n)      n*x^(n + 1)   x - x^(n + 1) - n*x^(n + 1) + n*x^(n + 2)
    U = -----------  -   ----------- = ----------------------------------------- =
         (1 - x)^2          1 - x                     (1 - x)^2
      x - (n + 1)*x^(n + 1) + n*x^(n + 2)                     x - inf + inf       x
    = ----------------------------------- = (n -> infinity) = ------------- = ---------
                  (1 - x)^2                                     (1 - x)^2     (1 - x)^2
        x
    --------- -> m, then x = m*(1-x)^2 = m*(1 - 2*x + x^2) = m - 2*m*x + m*x^2
    (1 - x)^2
    m*x^2 - (2*m + 1)*x + m = 0
    D = (-2*m - 1)^2 - 4*m^2 = 4*m^2 +4*m + 1 - 4*m^2 = 4*m + 1
             -(-2*m - 1) + (4*m + 1)^0.5  -(-2*m - 1) - (4*m + 1)^0.5
    x1, x2 = ---------------------------, ---------------------------
                        2*m                          2*m
                                                  2*m + 1 + (4*m + 1)^0.5         1     (4*m + 1)^0.5
    x1 is always greater than 1 because m > 0 and -----------------------  = 1 + --- +  -------------
                                                           2*m                   2*m         2*m
             2*m + 1 - (4*m + 1)^0.5
    Then x = -----------------------
                     2*m'''
    return (2*m + 1 - (4*m + 1)**0.5)/(2 * m)

print(solve(2))  # 0.5
print(solve(8))  # 0.7034648345913732