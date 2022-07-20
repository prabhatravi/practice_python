#direct method
l=[10,20,30,40,50]
d=2
l=l[d:]+l[:d]
print(l)

#use collection.deque
from collections import  deque
l=[10,20,30,40,50]
d=2

dq=deque(l)
dq.rotate(-d)
l =list(dq)
print(l)

#own method
def leftRotate(l,d):
    for i in range(0,d):
        l.append(l.pop(0))

l=[10,20,30,40,50]
d=2
leftRotate(l,d)
print(l)

#auxiliary space
def reverse(l,b,e):
    while b<e:
        l[b],l[e]=l[e],l[b]
        b=b+1
        e=e-1


def leftRotate(l,d):
    n=len(l)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
    reverse(l,0,n-1)


l=[10,20,30,40,50]
d=2
leftRotate(l, d)
print(l)
