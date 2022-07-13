set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c', 'd'}

# union
print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))

set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}
# intersection
print(set_A & set_B)
print(set_A.intersection(set_B))
print(set_B.intersection(set_A))

# difference
print(set_A - set_B)
print(set_A.difference(set_B))

print(set_B - set_A)
print(set_B.difference(set_A))