# RAHHH!!!!!

import math

e = 65537

p = -811

q = 0#??????

n = p * q

phi_n = (p + 1) * (q + 1) 

# but first, a word from
# our sponsored function!
def extendedEuclideanAlgo(e, phi_n):
    A1, A2, A3 = 1, 0, phi_n # var "b"
    B1, B2, B3 = 0, 1, e # var "a

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

def encrypt(int, e, n):
    return pow(int, e, -n)