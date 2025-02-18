import re

nums = []
with open("./log.txt", "r") as f:
    nums = re.findall(r"-?\d+", f.read())

output = b"Can birds even understand me?"

h = [0 for _ in range(len(output))]

t = 0
# Going through the input string first
for i in range(len(output) * 8):
    byte = i >> 3
    bitmask = 1 << (i & 7)
    # If this is a 1
    if output[byte] & bitmask:
        # Find out how far we had to shift it to make it be where it is
        j = i - int(nums[t])
        byte = j >> 3
        bitmask = 1 << (j & 7)
        h[byte] |= bitmask
        # Now consider the next bit
        t += 1

print(bytes(h).decode())
