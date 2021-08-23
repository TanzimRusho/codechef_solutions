# cook your dish here
import random
from collections import deque

def generateRandom(length):
    key = ""
    for i in range(length):
        temp = str(random.randint(0, 1))
        key += temp  
        
    return key

if __name__ == "__main__":
    t = int(input())
    
    for i in range(t):
        n = int(input())
        
        array = deque()
        
        for i in range(n):
            a = input()
            array.append(a)
        
        while True:
            key = generateRandom(n)
            if key in array:
                continue
            else:
                print(key)
                break
                    
