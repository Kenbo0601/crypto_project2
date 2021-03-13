import random
import secrets


def miller_rabin(n):  # miller rabin test
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
    while miller_rabin(var) == False:
        var = secrets.randbits(33)
        while len(bin(var)[2:]) < 33:
            var = secrets.randbits(33)
    # print(len(bin(var)[2:]))
    return var


def get_q(var):
    while var % 12 != 5:
        check = secrets.randbits(33)
        while len(bin(check)[2:]) < 33:
            check = secrets.randbits(33)
        # print(len(bin(check)[2:]))
        var = grab_prime(check)
    return var


def get_p(q):
    p = miller_rabin(2*q+1)
    if miller_rabin(p) == True:
        return p
    else:
        check = secrets.randbits(33)
        while len(bin(check)[2:]) < 33:
            check = secrets.randbits(33)
        prime = grab_prime(check)
        q = get_q(prime)
        while miller_rabin(2*q+1) == False:
            check = secrets.randbits(33)
            while len(bin(check)[2:]) < 33:
                check = secrets.randbits(33)
            prime = grab_prime(check)
            q = get_q(prime)
        return 2*q+1  # return p


def genKeys():
    var = secrets.randbits(33)
    while len(bin(var)[2:]) < 33:
        var = secrets.randbits(33)
    grab_prime(var)
    q = get_q(var)
    p = get_p(q)

    d = random.randrange(1, p-2)  # private key
    e2 = pow(2, d, p)  # public key
    return e2, d, p


def driver():
    keys = genKeys()
    e2 = str(keys[0])
    d = str(keys[1])
    p = str(keys[2])
    g = "2"  # generator

    # public key: p g e2
    # private key: p g d

    f = open("pubkey.txt", "w")
    f.write(p)
    f.write(" ")
    f.write(g)
    f.write(" ")
    f.write(e2)

    f2 = open("prikey.txt", "w")
    f2.write(p)
    f2.write(" ")
    f2.write(g)
    f2.write(" ")
    f2.write(d)

    f.close()
    f2.close()

    return


if __name__ == "__main__":
    driver()
