import bad_prng
import random

flag = ""

output = []
random = bad_prng.generate_seed()
for c in flag:
    random = bad_prng.rand_word()
    output.append(random ^ ord(c))

print(bytes(output).hex())
