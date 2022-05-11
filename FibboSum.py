n=int(input())
m=int(input())
n+=m+1
fib=lambda n:n if n<=1 else fib(n-1)+fib(n-2)
A=list(map(fib,range(0,n,1)))
print(A[-1])



# n=int(input())
# m=int(input())
# n+=m+1
# fib=lambda n:n if n<=1 else fib(n-1)+fib(n-2)
# A=list(map(fib,range(0,n,1)))
# print(A[-1])

