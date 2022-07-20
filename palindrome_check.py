st = "abba"
#while loop
s = 0
e = len(st)-1
while s < e:
    if st[s] != st[e]:
        print("No")
        break
    s += 1
    e -= 1
else:
    print("Yes")

#string slicing
st = "abcba"
if st == st[::-1]:
    print("Yes")
else:
    print("No")
