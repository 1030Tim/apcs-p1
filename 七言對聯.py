n = int(input())

for i in range(n):
    count = 0
    a1 = list(map(int,input().split()))
    a2 = list(map(int,input().split()))
    a1.insert(0,99)
    a2.insert(0,99)
    
    #狄摩根定律
    if not(((a1[2]!=a1[4])and(a1[2]==a1[6]))and(a2[2]!=a2[4])and(a2[2]==a2[6])):
        print("A",end="")
        count+=1
    if not((a1[-1]==1)and(a2[-1]==0)):
        print("B",end="")
        count+=1
    if not((a1[2]!=a2[2])and(a1[4]!=a2[4])and(a1[6]!=a2[6])):
        print("C",end="")
        count+=1

    if(count==0):
        print(None)
    else:print()

    

