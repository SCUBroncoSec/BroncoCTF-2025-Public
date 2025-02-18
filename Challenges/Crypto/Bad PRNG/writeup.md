# Info
Title: Mid PRNG
Flag: bronco{0k_1ts_n0t_gr34t}
# Challenge
This challenge is essentially an OTP break, but using PRNG that can be "easily" broken since you can just do simple regression on the values while they are increasing.
# Solution
First, notice that the first 7 random numbers can be found by xoring the values with the known string "bronco{".

Also, note that these numbers will never be greater than 255. Since there is XOR involved, the function either never goes beyond this point or is modulused by it.

Doing regression on the full set of elements gives nothing. The jumpy setup lends to the idea that it is modulus rather than a single function: this would be a ridiculous function.

So, it is assumed that the answer is a function modulus 256.

Looking at the knowable points should show the rough shape of the function.

Doing regression on the first elements (which is likely to be 2-3 elements along the real function, without modulus) should have several "perfect" regressions.

When done to multiple random sets, it can be seen that while each of the "perfect" regressions varies significantly or has very precise decimals.

However, using exponential regression shows that the base is ALWAYS 3, so this is likely the answer.

This can then be tested by solving for the next known characters.

Alternatively, some multiple of 256 can be added to each of the modulused numbers to try and find the unmodulused version. This can help check a regression.

After finding the function, it should be trivial to solve any given equation.
