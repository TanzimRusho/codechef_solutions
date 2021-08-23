# cook your dish here
from functools import reduce

t = int(input())

for i in range(t):
    n = int(input())
    array = [int(x) for x in input().split()]
    
    length = len(array)
    
    mode = max(set(array), key=array.count)
    
    xor_list = [num^mode for num in array]   
    
    res = reduce(lambda x, y: x|y, xor_list)
    
    print(mode, res)
