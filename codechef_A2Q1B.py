powers = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 
2281]

n = int(input())

for i in range(n):
    p = powers[i]
    print((2**(p-1))*(2**p-1))
