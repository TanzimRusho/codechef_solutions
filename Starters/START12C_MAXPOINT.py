t = int(input())

for case in range(t):
    mins = list(map(int, input().split()))
    points = list(map(int, input().split()))

    maxm = 0
    
    for i in range(21):
        for j in range(21):
            for k in range(21):
                if i*mins[0] + j*mins[1] + k*mins[2] <= 240:
                    maxm = max(i*points[0] + j*points[1] + k*points[2], maxm)
                    
    print(maxm)
