x=int(input())
n=list(map(int, input().split()))
dup_list = list(n)
n.sort()

res = abs(n[0]-n[2])

print(dup_list.index(res))