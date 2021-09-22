t = int(input())

for i in range(t):
    days = list(map(int, input().split()))
    count_1 = 0
    count_0 = 0
    
    for day in days:
        if day == 1:
            count_1 += 1 
        else:
            count_0 += 1 
            
    if count_1 > count_0:
        print("YES")
    else:
        print("NO")
