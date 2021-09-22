t = int(input())

for i in range(t):
    n = int(input())
    
    for num in range(10**(n-1), 10**n - 1):
        if num % 2 != 0 and num % 3 == 0 and num % 9 != 0: 
            print(num)
            break 
        
            
