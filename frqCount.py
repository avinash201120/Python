str1 = input("")
d=dict()
for c in str1:
    if c in d:
        d[c]=d[c]+1
    else:
        d[c]=1
res=""
for item in d:
    res += item + str(d[item])
print(str(res))                
