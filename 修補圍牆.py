n = int(input())
k = list(map(int,input().split()))
count = 0

if k[0] == 0:
    k[0] = k[1]
    count+=k[0]

for i in range(1,n-1):
    if k[i]==0:
        if k[i-1]<k[i+1]:
            k[i] = k[i-1]
            count+=k[i]
        else:
            k[i] = k[i+1]
            count+=k[i]
if k[-1]==0:
    k[-1] = k[-2]
    count+=k[-1]
print(count)