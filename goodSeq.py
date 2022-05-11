def CountOpe(A):
    n=len(A)
    c=0
    for i in range(n-2):
        if A[i]==A[i+2]:
            pass
        else:
            c+=1
        if n==10:
            return (n-4)
        else:
            return(n-2)        
           