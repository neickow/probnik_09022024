for A in range(0, 500):
    i=0
    for x in range(0, 500):
        for y in range(0, 500):
            if (x>39) or (y>26) or (2*x+4*y<A):
                i+=1
    if i==500**2:
        print(A)
        break