b = 6500 + 100000
c = b + 17000
h = 0
g = 2
while True:
    f = 1
    d = 2
    while g != 0:
        if b % d == 0:
            f = 0
        d += 1
        g = d - b
    if f == 0:
        h += 1
    g = b - c
    print(g)
    if g == 0:
        print(h)
        exit()
    b += 17
