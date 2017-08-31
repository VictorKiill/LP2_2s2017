def middle_way(a, b):
    c = []
    if len(a)%2 == 1 and len(b)%2 == 1:
        ac = a[len(a)//2]
        bc = b[len(b)//2]
        c.extend([ac, bc])
    return c