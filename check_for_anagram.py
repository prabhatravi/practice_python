s1= "listen"
s2= "silent"

def areAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    s1=sorted(s1)
    s2=sorted(s2)
    return(s1==s2)

def areAnagram_1(s1,s2):
    if len(s1) != len(s2):
        return False
    count=[0]*256
    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1
    for x in count:
        if x!=0:
            return False
    return True

def isAnagram(a,b):
    #code here
    if len(a) != len(b):
        print("NO")
        return
    count = [0]*256
    for i in range(len(a)):
        count[ord(a[i])]+=1
        count[ord(b[i])]-=1
    for x in count:
        if x!=0:
            print("NO")
            return
    print("YES")
    return

print(areAnagram(s1, s2))
print(areAnagram_1(s1, s2))
isAnagram(s1, s2)