a,b,c = sorted([int(_) for _ in input().split()],reverse = True)
# 7 9 7 -> 9 7 7
if a==b==c:
    print(3,a)

if a==b!=c:
    print(2,a,c)

if a!=b and b==c:
    print(2,a,b)
if a!=b and b!=c:
    print(1,a,b,c)
