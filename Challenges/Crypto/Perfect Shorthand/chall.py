import random

s = ""
with open("./phonetics.txt") as f:
    s = f.read().lower()

ignore = "“.?!(),\n:— -”;"
map = {}
for c in s:
    if c in ignore:
        continue

    if c not in map:
        map[c] = 0

    map[c] += 1

print(map)
l = [s[i] for i in range(len(s))]
cm = [chr(65+i) for i in range(len(map.keys()))]
random.seed(105)
random.shuffle(cm)
for i,k in enumerate(map.keys()):
    for j,c in enumerate(s):
        if c == k:
            l[j] = cm[i]

print("".join(l))
