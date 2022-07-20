s1 = "GeeksforGeeks"
s2 = "GrGes"
i, j = 0, 0
while i < len(s1) and j < len(s2):
    if s1[i] == s2[j]:
        j = j+1
    i = i+1

if j == len(s2):
    print(True)
else:
    print(False)
