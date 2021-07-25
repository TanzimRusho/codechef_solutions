t = int(input())

for i in range(t):
    n, k = input().split()
    n = int(n)
    k = int(k)
    
    A = [i for i in range(2**n)]
    
    length = len(A)
    maxm = 0
    
    while k != 0:
        for i in range(length):
            for j in range(i, length):
                A[i], A[j] = A[j], A[i]
                
        xor_list = [A[i] ^ i for i in range(length)]
        if sum(xor_list) > maxm:
            maxm = sum(xor_list)
            
        k -= 1     
        
    print(maxm)
    
    #print(sum(xor_list))
                
    
    
    
        
