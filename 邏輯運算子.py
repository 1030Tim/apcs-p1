a,b,c = [int(_) for _ in input().split()]

a = bool(a)
b = bool(b)
c = bool(c)

if ( (a and b) == c):
    print("AND")
if ( (a or b) == c):
    print("OR")
    
if ( (a != b)==c):
    print("XOR")

if ( (a==False)and(b==False)and(c==True)):
    print("IMPOSSIBLE")


