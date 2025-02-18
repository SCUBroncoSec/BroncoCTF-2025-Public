input = "dvlby_otspnr{cobrnot450i1nm_e03}"
s = ""
mid = len(input) // 2 - 1
# Undoes the original
# Can also be solved pen-and-paper by drawing circles
for i in range(len(input)):
    i += 1
    if i % 2 == 0:
        s += input[mid + i // 2]
    else:
        s += input[mid - i // 2]


print(s)
