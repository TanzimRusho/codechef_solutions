import math

t = int(input())

#print(math.ceil(4.5))

for i in range(t):
    n, k = input().split()
    n = int(n)
    k = int(k)
    
    a = max(n, k)
    b = min(n, k)
    maxm = 0
    #count = 0

    for x in range(b, a+1):
        #print("Here")
        #print((b-x)/2, (x-a)/2)
        
        if math.ceil((b-x)/2) < 0:
             a, b = b, a
        elif math.ceil((x-a)/2) < 0:
             b, a = a, b
        
        num = math.ceil((b-x)/2) + math.ceil((x-a)/2)
        #print(num, end=" ")
        #count += 1
        if num > maxm:
            maxm = num
    
    print(maxm)
    

