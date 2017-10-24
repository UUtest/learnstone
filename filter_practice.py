def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    t = _odd_iter()
    while True:
        n = next(t)
        yield n
        t = filter(_not_divisible(n), t)
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
