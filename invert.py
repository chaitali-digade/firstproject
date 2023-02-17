s='aaaabbbbbcccccc'
ch=s[0]
count=1
output=' '
i=1
while i<len(s):
    if ch==s[i]:
        count=count+1
    else:
        output=output+ch+s(count) 
        
    
    i=i+1 
output=output+ch+str(count) 
print(output)        