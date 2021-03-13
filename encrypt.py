import random
from os import path


def converter():
    f = open("ptext.txt", "r")
    char = f.read()
    list = []
    fulltext = ""
    for i in char:
        list.append(i)
        if " " in list:
            list.remove(" ")
    fulltext = "".join(list).strip("\n")
    f.close()
    list.clear()

    for j in range(0, len(fulltext), 4):
        list.append(fulltext[j:j+4])

    arr = []
    result = []
    for i in list:
        arr.clear()
        for c in i:
            temp = ord(c)
            arr.append(bin(temp)[2:].zfill(8))
        result.append(int("".join(arr), 2))
    return result


def encrypt(p, e1, e2, P):
    r = random.randrange(1, p-1)
    c1 = pow(e1, r, p)
    tempP = P % p
    tempe2 = pow(e2, r, p)
    c2 = tempP*tempe2 % p
    return c1, c2


def driver(msg, p, g, e2):
    f = open("ctext.txt", "w")
    for i in range(len(msg)):
        cipher = encrypt(p, g, e2, msg[i])
        c1 = cipher[0]
        c2 = cipher[1]
        f.write(str(c1))
        f.write(" ")
        f.write(str(c2))
        f.write("\n")
    f.close()
    return


if __name__ == "__main__":
    msg = converter()
    char = ""
    f = open("pubkey.txt", "r")
    for i in f:
        char = i.split()
    f.close()
    driver(msg, int(char[0]), int(char[1]), int(char[2]))
