import random
from os import path


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


def genKeys(pvar):
    var = random.getrandbits(32)
    grab_prime(var)
    q = get_q(var)
    p = get_p(q)
    while p <= pvar:
        p = get_p(q)

    d = random.randrange(1, p-2)  # private key
    e2 = pow(2, d, p)  # public key
    return e2, d, p


def converter():
    f = open("plaintext.txt", "r")
    char = f.read()
    f.close()

    arr = []
    for c in char:
        temp = ord(c)
        arr.append(bin(temp)[2:].zfill(8))
    return int("".join(arr), 2)


def encryption(e1, e2, p, P):
    r = random.randrange(1, p-1)
    c1 = pow(e1, r, p)
    tempP = P % p
    tempe2 = pow(e2, r, p)
    c2 = tempP*tempe2 % p
    return c1, c2


def driver():
    msg = converter()
    keys = genKeys(msg)
    e2 = keys[0]
    d = keys[1]
    p = keys[2]
    cipher = encryption(2, e2, p, msg)
    c1 = cipher[0]
    c2 = cipher[1]

    if path.exists("ctext.txt"):
        print("the file exists")
    else:
        print("nope")

    return


if __name__ == "__main__":
    driver()

    #t1 = pow(c1, p-1-d, p)
    #t2 = c2 % p
    #P = t1*t2 % p
