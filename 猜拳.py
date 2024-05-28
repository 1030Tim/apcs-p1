f = int(input())
n = int(input())
loss = win = tie = 0

k = list(map(int,input().split()))

for i in range(n):
    print(f,end=" ")
    if (k[i] == 2):
        if (f == 0):
            
            win+=1
            break
        elif (f==5):
            loss+=1
            break
        else:tie+=1
        
    elif (k[i] == 0):
        if (f==5):
            win+=1
            break
        elif (f==2):
            loss+=1
            break
        else:tie+=1

    elif (k[i] == 5):
        if (f==2):
            win+=1
            break
        elif (f==0):
            loss+=1
            break
        else:tie+=1
    if (tie==2):
        if(k[i] == 5):f=2
        elif(k[i] == 2):f=0
        elif(k[i] == 0):f=5
        tie = 0
    
if win!=0:
    print(f": Won at round {i+1}")
elif loss!=0:
    print(f": Lost at round {i+1}")
else:
    print(f": Drew at round {n}")
