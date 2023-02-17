s="chaitali gayatri ankita sonu chaitali gayatri dhanu"
l=s.split()
d={}

for word in l:
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1    

print(d)
