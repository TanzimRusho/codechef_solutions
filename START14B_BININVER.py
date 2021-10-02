from fractions import gcd
from collections import deque
from functools import reduce

def divide_2(nums):
    a = deque()
    
    for elem in nums:
        a.append(elem // 2) 
        
    return a 

t = int(input())

for i in range(t):
    n = int(input())
    
    array = tuple(map(int, input().split()))
    
    count = 0 
    
    while True:
        if (reduce(gcd, array)) % 2 == 1:
            break 
        
        else:
            array = divide_2(array)
            count += 1 
            
    print(count)

    
    