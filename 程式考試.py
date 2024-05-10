n = int(input())
arr = [ ]
n_max = -10000**2
count = 0
u = 0
for i in range(n):
    x,y = [int(_) for _ in input().split()]
    if y>n_max:
        n_max = y
        u = x
    if y == -1:count+=1

k = ((n_max-n)-count*2)
if k<=0:k = 0
print(k,u)