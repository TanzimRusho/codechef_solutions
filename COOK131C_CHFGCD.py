def gcd(a, b):
    while(b):
        a, b = b, a%b

    return a    
    
if __name__ == "__main__":
    t = int(input())
    
    for i in range(t):
        x, y = input().split()
        x, y = int(x), int(y)
        
        flag = True
        if x%2 == 0 and y%2==0:
            print(0)
            flag = False
        elif x%2 == 0 and y%2 != 0:
            if gcd(x, y) == 1:
                print(1)
                flag = False
            else:
                print(0)
                flag = False
        elif x%2 != 0 and y % 2 == 0:
            if gcd(x, y) == 1:
                print(1)
                flag = False
            else:
                print(0)
                flag = False
        elif x%2 != 0 and y % 2 != 0:
            if gcd(x, y) > 1:
                print(0)
                flag = False
            else:
                if gcd(x, y) == 1:
                    x += 1
                    if gcd(x, y) > 1:
                        print(1)
                        flag = False
                    else:
                        x -= 1
                        y += 1
                        if gcd(x, y) > 1:
                            print(1)
                            flag = False
        
        if flag:
            print(2)
