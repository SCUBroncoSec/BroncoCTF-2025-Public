import random

MOD = 2 ** 8
BASE = 3

# Valid seeds. These contain between 2 and 3 elements which follow the pattern
seeds = [10,11,13,14,15,17,18,19,21,22,23,25,26,27,29,30,31,33,34,35,37,38,39,41,42,43,45,46,47,49,50,51,53,54,55,57,58,59,61,62,63,65,66,67,69,70,71,73,74,75,77,78,79,81,82,83,85,87,89,90,91,93,94,105,115,143,145,162,173,174,175,177,178,179,181,190,201,202,209,219,229,230,238,247]

seed = 0

def scramble(num):
    return BASE * num % MOD

def rand_word():
    global seed
    value = seed
    seed = scramble(seed)
    return value

def generate_seed():
    global seed

    seed = random.choice(seeds)

generate_seed()
