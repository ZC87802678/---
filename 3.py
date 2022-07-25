list_1 = [1, 2, 3, 4]
count = 0
for c in list_1:
    for r in list_1:
        for x in list_1:
            if (c != r) and (c != x) and (r != x):
                count += 1
                print(c, end="")
                print(r, end="")
                print(x, end="")
