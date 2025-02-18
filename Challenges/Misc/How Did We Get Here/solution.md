# How Did We Get Here

## Flag

bronco{wh4t_th3_f0ck_1s_RSA}

## Intended Solution:

Answer to #1: **Rafael** Nadal

Answer to #2: Luis **Peralta**

Look up Rafael Peralta on wikipedia: [https://en.wikipedia.org/wiki/Rafael_Peralta](https://en.wikipedia.org/wiki/Rafael_Peralta)

We will use his birth day (7) and birth year (1979) in RSA: [https://www.cs.drexel.edu/~popyack/Courses/CSP/Fa17/notes/10.1_Cryptography/RSA_Express_EncryptDecrypt_v2.html](https://www.cs.drexel.edu/~popyack/Courses/CSP/Fa17/notes/10.1_Cryptography/RSA_Express_EncryptDecrypt_v2.html)

    1. Using p = 7 and q = 1979, we get n = 13853.

    2. Then, the first candidate for k = 11869.

    3. Factoring, we get e = 143, d = 83.

    4. Then, we can decode the message using n = 13853 and d = 83 to get the flag.

Nice and simple!
