from itertools import takewhile
import itertools

def primes():
    a = 2
    yield a
    while True:
        a += 1
        if a % 2 == 1:
            yield a

ge = primes()

print(list(itertools.takewhile(lambda x : x < 31, primes())))
#
# for i in range(60):
#     print(next(ge))

