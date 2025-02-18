flag = "bronco{tr4n5p0sit1on_my_bel0v3d}"
s = ""

for i, c in enumerate(flag):
    # Switch between adding before and after the rest of the characters
    if i % 2 == 0:
        s = c + s
    else:
        s = s + c

print(s)
