txt = "GeeksForGeeks"
pat = "Geeks"

pos = txt.find(pat)

while pos>=0:
    
    print(pos)
    pos = txt.find(pat,pos+1)