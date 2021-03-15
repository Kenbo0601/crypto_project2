# CS485 Cryptosystem

Kenichi Sakamoto  
kenichi2@pdx.edu  
course section - CS485  


Implementation of a public key encryption called Cryptosystem.  
The algorithm is similar to the Digital signature algorithm.  

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

### Source code for Miller Rabin prime number test
https://qiita.com/srtk86/items/609737d50c9ef5f5dc59
