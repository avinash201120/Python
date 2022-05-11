def InversionCount(A,n):
    if len(A)==0:
        return(-1)
    elif n<2:
        return(0)
    else:
        count=0
        for i in range(len(A)):
            j=i+1
            while(j<len(A)):
                if A[i]>A[j]:
                    count=count+1
                j=j+1
        return(count) 

n = int(input(""))
A = list(int(num) for num in input("").strip().split())[:n]

print(InversionCount(A,n))                          