# Rahhh-SA

## Flag
bronco{m4th3m4t1c5_r34l1y_1s_qu1t3_m4g1c4l_raAhH!}

## Intended Solution:
This is simply an implementation of the RSA public key cryptosystem except for 2 things:

1. Negative numbers are used for `p` and `q` (one number has to be provided in order for this to be understood) 
2. The `n` used during the encryption/decryption operation is the negative version.

Aspect 1 doesn't really change much. `n = p * q` will be a positive number since two negatives multiplied together yield a positive number. The only thing to watch out for is `phi_n` - since these still use `p` and `q`, which are negative, we must now `+1` instead of `-1` so that the magnitude of the numbers go down as intended. One can also just forego the negative `p` given in the prompt by turning it into a positive and performing `(p-1)(q-1)` for `phi_n` like normal RSA. Math is magical like that!

Aspect 2, however, cannot be bypassed. `-n` was used in the exponentiation, and since the ciphertext was generated with this, `-n` must be used during decryption too.

After figuring out the negative schemes going on, the challenge mostly boils down to a RSA decryption exercise. Any tool for this works.

The following script was used to generate this challenge. It is the full, non-shortened, non-redacted version of the source code given in the prompt.
```py
import math

e = 65537

p = -811
q = -4229

n = p * q
print("n", n) # 3429719

phi_n = (p + 1) * (q + 1) 
print("phi_n", phi_n) # 3424680

def extendedEuclideanAlgo(e, phi_n):
    A1, A2, A3 = 1, 0, phi_n # b
    B1, B2, B3 = 0, 1, e # a

    while (True):
        if B3 == 0:
            return -1 
            # indicates no inverse!
        if B3 == 1:
            return B2 
            # B2: modular inverse

        Q = math.floor(A3 / B3)
        T1, T2, T3 = A1 - (Q * B1), A2 - (Q * B2), A3 - (Q * B3)
        A1, A2, A3 = B1, B2, B3
        B1, B2, B3 = T1, T2, T3

inv = extendedEuclideanAlgo(e, phi_n)
d = inv % phi_n # need to modulo by phi_n for correct result! 
print("d", d) # 1759553

def encrypt(int, e, n):
    return pow(int, e, n)

def decrypt(cText, d, n):
    return pow(cText, d, n)

flag = "bronco{m4th3m4t1c5_r34l1y_1s_qu1t3_m4g1c4l_raAhH!}"

cipherInts = []
for each in flag:
    res = encrypt(ord(each), e, n)
    cipherInts.append(res)
    print(ord(each), " -> ", res)

print(cipherInts)

plainInts = []

for each in cipherInts:
    res = pow(each, d, n)
    plainInts.append(res)
    print(each, " -> ", res)

plaintext = ""

for pInt in plainInts:
    print(pInt, " -> ", chr(pInt))
    plaintext = plaintext + chr(pInt)

print(plaintext)
```