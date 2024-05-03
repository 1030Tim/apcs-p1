#https://zerojudge.tw/Submissions

def thefunction(k):
    c = {(0,1,0,1):"A",
         (0,1,1,1):"B",
         (0,0,1,0):"C",
         (1,1,0,1):"D",
         (1,0,0,0):"E",
         (1,1,0,0):"F"}
    return c[k]


while (1):
    try:
        n = int(input())
        acc = [ ]
        for i in range(n):
            k = tuple(map(int,input().split()))

            arr = thefunction(k)
            acc.append(arr)
        for i in range(len(acc)):
            print(acc[i],end="")

        print()
    except:
        break
