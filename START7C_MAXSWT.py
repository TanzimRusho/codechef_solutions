t = int(input())

for i in range(t):
    n, d = input().split()
    n = int(n)
    d = int(d)
    
    price = [int(x) for x in input().split()]
    sweet = [int(x) for x in input().split()]
    
    #for j in range(n):
    #    for k in range(j+1, n):
            
    # for pri, swe in zip(price, sweet):
    #     spp = swe/pri
    
    #spp = [swe/pri for pri, swe in zip(price, sweet)]
    #spp = sorted(spp, reverse=True)
    
    sum_swe = 0
    p = 0
    maxm = 0
    total_price = 0
    #while total_price <= d and count <=2:
    for j in range(n):
        for k in range(j+1, n):    
            #sum_swe += spp[p] * price 
            sum_swe = sweet[j] + sweet[k] 
            total_price =  price[j] + price[k]
            if sum_swe > maxm and total_price <= d:
                maxm = sum_swe
            #count += 1
                
    print(maxm)