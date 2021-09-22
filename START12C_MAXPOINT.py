t = int(input())

for i in range(t):
    mins = list(map(int, input().split()))
    points = list(map(int, input().split()))
    
    max_point = max(points)
    min_point = min(points)
    
    sum_time = 0
    sum_point = 0  
    
    for pat, point in zip(mins, points):
        if point == max_point:
            
            sum_time += pat * 20 
            sum_point += max_point * pat 
            
            print(sum_point)
            
        elif point not in [max_point, min_point]:
            item_left = 20 
            
            while sum_time != 240 or item_left != 0:
                sum_time += pat 
                sum_point += point 
                item_left -= 1 
            
            print(sum_point)
                
        elif point == min_point: 
            item_left = 20 
            
            while sum_time != 240 or item_left != 0:
                sum_time += pat 
                sum_point += point 
                item_left -= 1 
            
            print(sum_point)
            
    print(sum_point)
        
    
    
    