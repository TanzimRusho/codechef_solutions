T = int(input())

for i in range(T):
    a, b, c, d, e, f = input().split()
    a, b, c, d, e, f = int(a), int(b), int(c), int(d), int(e), int(f) 
    
    if a+b+c > d+e+f:
        print(1)
    else:
        print(2)
    
