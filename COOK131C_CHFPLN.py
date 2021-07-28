t = int(input())

for i in range(t):
    n = int(input())
    array = [int(x) for x in input().split()]
    
    length = len(array)
    
    points = []
    
    for j in range(length):
        for num in range(1, array[j]):
            (x, y) = (num, array[j]-num)
            points.append((x,y))
            
    
    points = list(set(points))
    
    print(len(points))
        
                
            