# m=int(input())
# c=0
# while m>0:
#     if m%2==0:
#         m//=2
#         c+=1
#     else:
#         m-=1
#         c+=1
# print(c)

def code(m):
    # m=int(input())
    c=0
    while m>0:
        if m%2==0:
            m//=2
            c+=1
        else:
            m-=1
            c+=1
    return c
m=int(input())
print(code(m))   
           
