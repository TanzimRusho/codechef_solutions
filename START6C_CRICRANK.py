T = int(input())

for i in range(T):
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    score_A = 0
    score_B = 0
    
    for i, j in zip(A, B):
        if i > j:
            score_A += 1
        elif i < j:
            score_B += 1
        else:
            continue

    if score_A > score_B:
        print("A")
    else:
        print("B")
            
