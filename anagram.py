n=input()
m=input()
count=0
l=len(m)
for i in n:
    if i in m:
        count=count+1
    else:
        pass
if count == l:
    print("Yes")
else:
    print("No")           