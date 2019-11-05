"""Description

A prime number is an integer greater than 1 that is only evenly divisible
by itself and 1.
Write your own Primes class with class method Primes.first(n) that returns
an array of the first n prime numbers."""


class Primes(object):
    cache = [2]
    checking = 3

    @classmethod
    def first(cls, n):
        while len(cls.cache) < n:
            is_prime = True
            i = 0
            root = cls.checking ** 0.5 + 1
            while i < len(cls.cache) and cls.cache[i] <= root:
                if not cls.checking % cls.cache[i]:
                    is_prime = False
                    break
                i += 1
            if is_prime:
                cls.cache.append(cls.checking)
            cls.checking += 2
        return cls.cache[:n]


print(Primes.first(5))  # [2, 3, 5, 7, 11]
print(Primes.first(20)[-5:])  # [53, 59, 61, 67, 71]
print(Primes.first(100)[99])  # 541
print(Primes.first(34)[29])  # 113
