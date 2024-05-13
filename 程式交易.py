n,d = [int(_) for _ in input().split()]
k = True
b = list(map(int,input().split()))
money = 0
y = 0
x = b[0]
for i in range(n):
    y = b[i]
    if (k == True and y>=x+d):
        money += abs(y-x)
        x = y
        k = False
    elif (k==False and y<=x-d):
        x = y
        k = True

print(money)