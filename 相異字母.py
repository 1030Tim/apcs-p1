n = int(input())
d = None
count_d =  float('inf')
for i in range(n):
    k = input()
    k1 = list(k)
    k1 = sorted(k)
    count = 0
    for j in range(1,len(k1)):
        if (k1[j-1]!=k1[j]):count+=1

    if (count<count_d):
        count_d = count
        d = k
   

    
    elif (count_d == count):
        if(k<d):
            d = k
            count_d = count
        else:
            count_d = count
       
    
print(d)

