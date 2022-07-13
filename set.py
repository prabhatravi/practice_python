random_set = {"Prabahat_Ravi", 1408, 3.142,
              (True, False)}
print(random_set)
print(len(random_set))  # Length of the set

# set() contructor
random_set = set({"PrabhatRavi", 1988, 7.8, (True, False)})
print(random_set)

# empty set
empty_set = set()
print(empty_set)
# add element
empty_set.add(1)
print(empty_set)
# update element
empty_set.update([2, 3, 4, 4, 5])
print(empty_set)
# delete element
empty_set.discard(4)
print(empty_set)
empty_set.remove(3)
print(empty_set)

odd_list = [9, 5, 7, 11]
# iterate the set
for num in empty_set:
    if (not num%2 == 0):
        odd_list.append(num)

print(odd_list)

