#取1-100的奇数:
'''L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L) 
'''
#取L的前一半：
'''
#1:
L = list(range(1,100,2))
print(L[:len(range (1,100,2)) // 2])
'''
#2:
print([n for n in range(1, 99, 2) if n <= len(range(1, 99, 2))])
