t = int(input())

for i in range(t):
    a, b, c = input().split()
    if a == "1" and b == "1" and c == "1":
        print(0)
    elif a == "0" and b == "0" and c == "0":
        print(0)
    else:
        print(1)
        
