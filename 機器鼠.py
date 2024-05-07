x,n = [int(_) for _ in input().split()]
k = list(map(int,input().split()))
arr = [int(u) for u in k if u >=x]
acc = [int(u) for u in k if u<x]
arr.sort()
acc.sort()
if len(arr)>len(acc):
    print(len(arr),arr[-1])
else:
    print(len(acc),acc[0])