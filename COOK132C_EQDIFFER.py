t = int(input()) 

for i in range(t):
    n = int(input())
    
    array = [int(x) for x in input().split()]
    
    if n == 1 or n == 2:
        print(0)
        continue
           
    dict_ = {}
    
    for i in array:
        if i not in dict_:
            dict_[i] = 1 
        else:
            dict_[i] += 1 
            
    max_ = 0
    
    for i, j in dict_.items():
        max_ = max(max_, j)
        
    if max_ == 1:
        print(n-2)
    else:
        print(n-max_)
