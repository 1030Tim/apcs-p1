a,b = [int(_)for _ in input().split()]
n = int(input())

count = 0
for i in range(n):
    k = list(map(int,input().split()))
    a_count = 0
    b_count = 0
    for j in k:
        if j!=0:
            if j == a:
                a_count+=1
            elif j == -a:
                a_count-=1
            elif j == b:
                b_count+=1
            elif j == -b:
                b_count-=1
    if a_count>0 and b_count>0:
        count+=1

print(count)