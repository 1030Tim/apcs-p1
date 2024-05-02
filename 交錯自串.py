n = int(input())#input
count = 10000
arr = [ ]

for i in range(n):
    k = list(map(str,input()))
    k_sort = k[:]
    
    k_sort.sort()
    
    c = 0
    t = k_sort[0]
    for j in range(len(k)):
        if ( t != k_sort[j] ):
            c+=1
            t = k_sort[j]
    #loopend        
    if (c<count):
        count = c
        arr = k
    elif (c == count):
        if (arr>k):
            count = c
            arr = k
#loopend
for i in range(len(arr)):#output
    print(arr[i],end="")
print()
