import random


def converter():
    f = open("ptext.txt", "r")
    char = f.read()
    f.close()

    arr = []
    for c in char:
        temp = ord(c)
        arr.append(bin(temp)[2:].zfill(8))
    return int("".join(arr), 2)


def encrypt(p, e1, e2, P):
    r = random.randrange(1, p-1)
    c1 = pow(e1, r, p)
    tempP = P % p
    tempe2 = pow(e2, r, p)
    c2 = tempP*tempe2 % p
    return c1, c2


if __name__ == "__main__":
    msg = converter()
    char = ""
    f = open("pubkey.txt", "r")
    for i in f:
        char = i.split()
    f.close()

    #p = char[0], g = char[1], e2 = char[2]
    cipher = encrypt(int(char[0]), int(char[1]), int(char[2]), int(msg))
    c1 = cipher[0]
    c2 = cipher[1]
    f = open("ctext.txt", "w")
    f.write(str(c1))
    f.write(" ")
    f.write(str(c2))
