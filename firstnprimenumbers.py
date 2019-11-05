"""Description

A prime number is an integer greater than 1 that is only evenly divisible
by itself and 1.
Write your own Primes class with class method Primes.first(n) that returns
an array of the first n prime numbers."""


class Primes(object):
    cache = [2]

    @staticmethod
    def is_prime(ch):
        for i in range(2, ch // 2 + 1):
            if not ch % i:
                return False
        return True

    @classmethod
    def first(cls, n):
        checking = 3
        if len(cls.cache) > 1:
            checking = cls.cache[-1] + 2
        while len(cls.cache) < n:
            if cls.is_prime(checking):
                cls.cache.append(checking)
            checking += 2
        return cls.cache[:n]


print(Primes.first(5))  # [2, 3, 5, 7, 11]
print(Primes.first(20)[-5:])  # [53, 59, 61, 67, 71]
print(Primes.first(100)[99])  # 541
print(Primes.first(34)[29])  # 113
