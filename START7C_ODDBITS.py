t = int(input())

for i in range(t):
    num = int(input())
    if num == 2:
        print(1)
        continue
    
    sum_ = 0
    
    for i in range(1, num):
        #print(i, end=" ")
        binary = bin(int(i))
        #print()
        binary = binary[2:]
        #print(binary, end= " ")
        #print()
        length = len(binary)
        output = False
        
        for j in range(0, length, 2):
            #print()
            sum_ += int(binary[j])
            if sum_ >= num:
                output = True
                break
            
        if output:
            print(i)
            break

    #print(j+1)
        
