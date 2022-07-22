def print_repeated_element(l):
    d = {}
    m = []
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in l:
        if d[i] == 1:
            m.append(i)
    return m
    


l = [1,1,3,3,4,5]
print(print_repeated_element(l))