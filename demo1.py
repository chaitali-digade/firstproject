str1='m5h4y8'
output=' '
for i in str1:
    if i.isalpha( ):
        temp=i
    else:
        output=output+temp*int(i)

print(output)            