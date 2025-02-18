# Our given hex string
input = "23a326c27bee9b40885df97007aa4dbe410e93"
# Turning this into a string would cause encoding issues, so keep it as bytes
input = bytes.fromhex(input)
key = "Awesome!"
carry = 0
flag = ""

for i,c in enumerate(input):
    # These are basically the reverse of the original order
    # Maybe that's why it's called "reversing" :/
    b = c
    b ^= ord(key[i % len(key)])
    b -= carry
    b %= 256
    flag += chr(b)
    carry += c
    carry %= 256

print(flag)
