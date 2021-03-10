import binascii


def decrypt(p, d, c1, c2):
    t1 = pow(c1, p-1-d, p)
    t2 = c2 % p
    P = t1*t2 % p
    print(P)

    bits = bin(P)
    n = int(bits, 2)
    decipher = binascii.unhexlify('%x' % n).decode('utf-8')
    print(decipher)
    return


def driver():
    cipher = ""
    key = ""

    f = open("ctext.txt", "r")
    for i in f:
        cipher = i.split()
    f.close()

    k = open("prikey.txt", "r")
    for i in k:
        key = i.split()
    k.close()

    p = int(key[0])
    d = int(key[2])
    c1 = int(cipher[0])
    c2 = int(cipher[1])

    decrypt(p, d, c1, c2)
    return


if __name__ == "__main__":
    driver()
