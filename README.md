#CS485 Cryptosystem

Kenichi Sakamoto
kenichi2@pdx.edu
course section - CS485


Implementation of a public key encryption called Cryptosystem. 
The algorithm is similar to the Discrete Logarithm Problem. 

### How to Build
1: python3 geKey.py
    -   this program generates both public key and private key
2: python3 encrypt.py
    -   this program encrypts the message using the public keys
3: python3 decrypt.py
    -   this program decrypts the ciphertext using the private keys

### A list of files
    -   genKey.py 
    -   encrypt.py
    -   decrypt.py
    -   ptext.txt #plaintext message
    -   ctext.txt #ciphertext message
    -   dtext.txt #result of decrypting the ciphertext
    -   prikey.txt #contains private keys
    -   pubkey.txt #contains public keys
