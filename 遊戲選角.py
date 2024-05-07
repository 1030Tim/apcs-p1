n = int(input())
acc = [ ]
arr = [ ]
for  i in range(n):
    a,b = [int(_) for _ in input().split()]

    k = a**2+b**2
    c = [a,b]
    acc.append(k)
    arr.append(c)
    
indax_arr  = acc[:]
indax_arr.sort()
indax_arr = indax_arr[-2]
indax = 0
for i in range(n):
    if acc[i] == indax_arr:
        indax = i
        break
            
print(arr[indax][0],arr[indax][1])
