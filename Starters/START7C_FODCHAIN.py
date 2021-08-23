import math

t = int(input())

for i in range(t):
    a, b = input().split()
    a = int(a)
    b = int(b)

    res = a
    count = 0
    
    while res > 0:
        res = math.floor(a/b)
        a = res 
        count += 1
        
    print(count)
