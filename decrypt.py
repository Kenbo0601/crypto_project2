import binascii


def decrypt(p, d, c1, c2, file, textbox):  # decryption process
    t1 = pow(c1, p-1-d, p)
    t2 = c2 % p
    P = t1*t2 % p

    bits = bin(P)
    n = int(bits, 2)
    decipher = binascii.unhexlify('%x' % n).decode('utf-8')
    file.write(decipher)
    textbox.append(decipher)
    return


def driver():  # driver function
    cipher = ""
    key = ""
    list = []

    f = open("ctext.txt", "r")
    for i in f:
        cipher = i.split()
        list.append(cipher)
    f.close()

    k = open("prikey.txt", "r")
    for i in k:
        key = i.split()
    k.close()

    p = int(key[0])
    d = int(key[2])
    c1 = ""
    c2 = ""

    textbox = []
    file = open("dtext.txt", "w")
    for block in list:
        c1 = int(block[0])
        c2 = int(block[1])
        decrypt(p, d, c1, c2, file, textbox)
    file.close()
    text = "".join(textbox)
    print("Deccryption result: \n", text)  # print the result
    return


if __name__ == "__main__":
    driver()  # call driver function
