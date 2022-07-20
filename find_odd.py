def findOdd(l):
    res = 0

    for x in l:
        res = res ^ x

    return res

l = [int(x) for x in input().split(',')]
print(findOdd(l))