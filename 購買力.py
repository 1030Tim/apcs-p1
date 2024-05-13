#先搞懂題目在問什麼不撋不會對
n,d = [int(_)for _ in input().split()]
count = 0
b = 0
for i in range(n):
    k = list(map(int,input().split()))
    if max(k)-min(k)>=d:
        count+=1
        b+=sum(k)//3
print(count,b)
