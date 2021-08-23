t = int(input())

for i in range(t):
    a, b = input().split()
    a = int(a)
    b = int(b)
    
    c_lot = 6 - (a + b) 
    
    if c_lot <= 4 and c_lot > 0:
        print("{:.6f}".format(c_lot/6))
    else:
        print("0")
