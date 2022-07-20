#using loop
s = "Prabhat Ravi"

rev = ""

for i in s:
    rev = i+rev

print(rev)

#using slicing
print(s[::-1])