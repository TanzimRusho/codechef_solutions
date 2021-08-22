# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    a = input() 
    b = input()
    
    count = 0
    count01 = 0 
    count10 = 0
    count00 = 0 
    count11 = 0 
    
    for i, j in zip(a, b):
        if i == "0" and j == "0":
            count00 += 1 
            #print("case 1")
            if count00 > 0 and count11 > 0:
                count += 1 
                count11 -= 1 
                count00 -= 1 
                
        elif i == "1" and j == "1":
            #print("case 2")
            count11 += 1 
            if count11 > 0 and count00 > 0:
                count += 1 
                count11 -= 1 
                count00 -= 1 
                continue
                
            elif count00 == 0 and count11 > 1:
                count += 1 
                count11 -= 2 
                continue
            
            elif count11 > 0 and count01 > 0:
                count += 1 
                count11 -= 1 
                count01 -= 1 
                continue 
            
            elif count11 > 0 and count10 > 0:
                count += 1 
                count11 -= 1 
                count10 -= 1 

        elif i == "0" and j == "1":
            #print("case 3")
            count01 += 1  
            if count01 > 0 and count10 > 0: 
                count += 1
                count10 -= 1
                count01 -= 1
                continue
        
            elif count01 > 0 and count11 > 0:
                count += 1 
                count01 -= 1 
                count11 -= 1 
        
        elif i == "1" and j == "0":
            #print("case 4")
            count10 += 1  
            if count10 > 0 and count01 > 0: 
                count += 1
                count10 -= 1
                count01 -= 1
                continue
        
            elif count10 > 0 and count11 > 0:
                count += 1 
                count10 -= 1 
                count11 -= 1 
            
        #print(f"count {count}")    

            
    print(count)
