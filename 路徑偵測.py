n = int(input())
lift= right = back  = 0
N,S,W,E = 0,1,2,3
d = E
x1 = y1 = 0
for i in range(n):
    x2,y2 = [int(_) for _ in input().split()]
    if (y2>y1):#N
        if (d==E):
            lift+=1
        elif (d==W):
            right+=1
        elif (d==S):
            back+=1
        d = N
    elif (y2<y1):#S
        if(d==E):
            right+=1
        elif(d==W):
            lift+=1
        elif(d==N):
            back+=1
        d = S
    elif (x1>x2):#W
        if(d==E):
            back+=1
        elif(d==N):
            lift+=1
        elif(d==S):
            right+=1
        d = W
    elif (x1<x2):#E
        if(d==N):
            right+=1
        elif(d==S):
            lift+=1
        elif(d==W):
            back+=1
        d = E
    x1 , y1 = x2 , y2
print(lift,right,back)
