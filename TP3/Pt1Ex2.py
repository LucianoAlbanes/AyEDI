v1,v2,v3 = (1,2,3)
OE = int(0)


# ordena 3 numeros de mayor a menor
OE += 1
if v1 > v2:
    OE += 1
    if v1 > v3:
        OE += 1
        r1 = v1
        OE += 1
        if v2 > v3:
            OE += 2
            r2 = v2
            r3 = v3
        else:
            OE += 2
            r2 = v3
            r3 = v2
    else:
        OE += 3
        r3 = v2
        r2 = v1
        r1 = v3
else:
    OE += 1
    if v2 > v3:
        OE += 1
        r1 = v2
        OE += 1
        if v1 > v3:
            OE += 2
            r2 = v1
            r3 = v3
        else:
            OE += 2
            r2 = v3
            r3 = v1
    else:
        OE += 3
        r1 = v3
        r2 = v2
        r3 = v1
OE += 4
print(r1, r2, r3, OE)
