from itertools import takewhile
import itertools

def is_prostoe(num):
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True

def primes():
    a = 2
    yield a
    while True:
        a += 1
        if is_prostoe(a):
            yield a

ge = primes()

print(list(itertools.takewhile(lambda x : x < 31, primes())))
#
# for i in range(60):
#     print(next(ge))

