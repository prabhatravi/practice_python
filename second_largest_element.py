def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = l[0]
    slar = None
    for x in l[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar == None or slar < x:
                slar = x
    return slar

print("Enter the list element:")
l = [int(x) for x in input().split()]
print("\n")
print("Second largest element is: ", getSecMax(l))