l = [10, 20, 30, 40, 50, 25]
l.append(30)
print(l)
l.insert(1, 15)
print(l)
print(15 in l)
print(l.count(30))
print(l.index(30))
l.pop()
print(l)
l.remove(15)
print(l)
print(l[2:4])
print(l[0::2])
print(15 not in l)
print(20 in l)
l.sort()
print(l)
l_double = []
for n in l:
    l_double.append(n*2)
print(l)
print(l_double)
# list comprehension
l_new_double = [n*2 for n in l]
print(l_new_double)
# list comprehension
lNewDouble = [n*2 for n in l if n % 4 == 0]
print(lNewDouble)
# multiple lists
sum_l = [(n1, n2) for n1 in l_new_double for n2 in lNewDouble if n1+n2 > 100]
print(sum_l)