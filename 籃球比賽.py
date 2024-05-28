a1 = sum(list(map(int,input().split())))
b1 = sum(list(map(int,input().split())))
a2 = sum(list(map(int,input().split())))
b2 = sum(list(map(int,input().split())))

print(f"{a1}:{b1}")
print(f"{a2}:{b2}")


if (a1>b1 and a2>b2):
    print("Win")
elif (a1<b1 and a2<b2):
    print("Lose")
else:
    print("Tie")
