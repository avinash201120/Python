def Pent(n,a):
    a=sorted(a)
    i=0;q=0
    while(i<len(a)-1):
        q=q+abs(a[i]-a[i+1])
        i+=1
    return q
n=int(input(""))
a=list(map(int,input().split()))
print(Pent(n,a))        

