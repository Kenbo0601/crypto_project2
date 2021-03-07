import random
import sys


def is_prime(n):  # miller rabin test
    if n == 2:
        return True
    if n == 1 or n & 1 == 0:
        return False

    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for k in range(100):
        a = random.randint(1, n - 1)
        t = d
        y = pow(a, t, n)

        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1

        if y != n - 1 and t & 1 == 0:
            return False

    return True


def grab_prime(var):
    while is_prime(var) == False:
        var = random.getrandbits(32)
    return var


def get_q(var):
    while var % 12 != 5:
        var = grab_prime(random.getrandbits(32))
    return var


def get_p(q):
    p = is_prime(2*q+1)
    if is_prime(p) == True:
        return p
    else:
        prime = grab_prime(random.getrandbits(32))
        q = get_q(prime)
        while is_prime(2*q+1) == False:
            prime = grab_prime(random.getrandbits(32))
            q = get_q(prime)
        return 2*q+1  # return p


def genKeys():
    var = random.getrandbits(32)
    grab_prime(var)
    print("prime:", var)

    q = get_q(var)
    p = get_p(q)
    d = random.randrange(1, p-2)
    e2 = pow(2, d, p)
    return e2,d


if __name__ == "__main__":
    var = genKeys()



