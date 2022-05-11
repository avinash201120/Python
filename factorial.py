m = int(input())
n = int(input())
fact = 1
fact1 = 1
for i in range(1,m+1):
    fact *=i
for i in range(1,n+1):
    fact1*=i
print(fact//fact1)        

# def Fact(n,m):
#     x = 1
#     y = 1
#     for i in range(1,n+1):
#         x = x * 1
#     for i in range(1,m+1):
#         y = y * i
#     return (x//y) 
# n=int(input(""))
# m=int(input(""))
# print(Fact(n,m))
# # print(Fact(m))     

