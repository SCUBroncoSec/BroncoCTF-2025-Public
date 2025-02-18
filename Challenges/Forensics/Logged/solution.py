import re
# Recognizing that this is an xev dump
print(":exe \"normal ", end="")
with open("keys.log") as f:
    for l in f:
        if l.startswith("KeyPress"):
            m = re.search(r"\(keysym (.+)\)", l)
            if m is not None:
                keysym = int(m.group(1), 16)
                if 32 <= keysym < 128:
                    print(chr(keysym), end="")
                # ESC
                elif keysym == 65307:
                    print("\\<esc>", end="")
                # Enter
                elif keysym == 65293:
                    print("\\<cr>", end="")
                # Right
                elif keysym == 0xff51:
                    print("\\<Left>", end="")
                # Backspace
                elif keysym == 0xff08:
                    print("\\<bs>", end="")
                # Left
                elif keysym == 0xff53:
                    # print("\032", end="")
                    print("\\<Right>", end="")
                # Super (oops)
                elif keysym == 0xffeb:
                    pass
                # Lshift
                elif keysym == 0xffe1:
                    pass
                # Rshift
                elif keysym == 0xffe2:
                    pass
                else:
                    print(hex(keysym))
                    pass
print("\"")
