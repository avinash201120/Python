def Character(input1,n):

    res=""

    for i in range(0,len(input1)):

        if input1[i].isalpha():

            res+=input1[i]*int(input1[i+1])

    if(n<=len(res)):

        return res[n]

    else:

        return -1
m=input()
a=int(input())
print(Character(m,a))		
