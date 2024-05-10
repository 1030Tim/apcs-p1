n = int(input())
ord_x , ord_y = [int(_) for _ in input().split()]

max_count = -10000
min_count = 99

for i in range(1,n):
    a,b = [int(_) for _ in input().split()]

    
    k = (abs(ord_x - a)+abs(ord_y - b))

    if k>max_count :max_count = k
    if k<min_count :min_count = k

    ord_x , ord_y = a,b


print(max_count,min_count)    
