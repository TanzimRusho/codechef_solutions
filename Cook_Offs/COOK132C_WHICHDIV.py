# cook your dish here
t = int(input())

for i in range(t):
    a = int(input())
    
    if a >= 2000:
        print(1)
    elif a >= 1600 and a < 2000:
        print(2)
    elif a < 1600:
        print(3)
