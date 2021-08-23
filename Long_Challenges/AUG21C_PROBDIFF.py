t = int(input())

for i in range(t):
    ques = [int(x) for x in input().split()]

    if len(set(ques)) == 4:
        print(2)
        continue
    
    elif len(set(ques)) == 1:
        print(0)
        continue

    seen = {}
    
    for i in range(4):
        if ques[i] not in seen:
            seen[ques[i]] = 1
        else:
            seen[ques[i]] += 1
            
    for elem in seen:
        if seen[elem] == 3:
            print(1)
            break
        elif seen[elem] == 2:
            print(2)
            break
            
    
