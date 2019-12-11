"""Description

The Fibonacci numbers are the numbers in the following integer sequence (Fn):
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
such as
F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
Given a number, say prod (for product), we search two Fibonacci numbers F(n)
and F(n+1) verifying
F(n) * F(n+1) = prod.
Your function productFib takes an integer (prod) and returns an array:
[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.
If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will
return [F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(m) being the smallest one such as F(m) * F(m+1) > prod.
Notes: Not useful here but we can tell how to choose the number n up to which to
go: we can use the "golden ratio" phi which is (1 + sqrt(5))/2 knowing that F(n)
is asymptotic to: phi^n / sqrt(5). That gives a possible upper bound to n.
References:
http://en.wikipedia.org/wiki/Fibonacci_number
http://oeis.org/A000045"""


def product_fib(prod):
    f0, f1 = 0, 1
    while f0*f1 < prod:
        f0, f1 = f1, f0 + f1
    if f0*f1 == prod:
        return [f0, f1, True]
    return [f0, f1, False]


print(product_fib(714))  # [21, 34, True]
print(product_fib(800))  # [34, 55, False]
