b = 6500 + 100000
c = b + 17000
h = 0
g = 2
while True:
    f = 1
    d = 2
    while g != 0:
        e = 2
        g = d
        while g != 0:
            g = d * e - b
            if g == 0:
                f = 0
            e += 1
            g = e - b
        d += 1
        g = d - b
        print(g)
    if f == 0:
        h += 1
    g = b - c
    if g == 0:
        print(h)
        exit()
    b += 17
