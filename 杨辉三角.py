# -*- coding: utf-8 -*-
def triangles():
    L = [1]
    while True: #进入持续循环
        yield L
        L.append(0) #1) 利用尾部插入0来控制第一位和最后一位值始终为1；
                    #2) 同时也是为了保证每一行的数值个数正确，因为后面有用到len(L)
                    #    来确定每次生成L的最终长度。
        L = [L[i - 1] + L[i] for i in range(len(L))]

#while的执行分解为简单的步骤：
'''
while True:
    yield L
    L.append(0)
    length = len(L)
    new_L = []
    for i in range(length):
        new_L.append(L[i-1]+L[i])
    L = new_L

第一次打印出的步骤： #不进行循环
L = [1]

第二次打印的步骤：

while True：
    yield L         
    L = [1, 0]
    length = 2
    for i in [0, 1]:
    new_L.append(L[-1] + L[0]) #第一次循环为1 
    new_L.append(L[0] + L[1])  #第二次循环为1
    L = new_L = [1，1]
第三次打印步骤：

while True:     
    yield L            
    L= [1, 1, 0]
    length = 3
    for i in [0, 1, 2]:
    new_L.append(L[-1] + L[0]) #第一次循环为1
    new_L.append(L[0] + L[1])  #第二次循环为2
    new_L.append(L[1] + L[2])  #第三次循环为1
    L = new_L = [1, 2, 1]
第四次打印步骤：

while True:
    yield L
    L = [1, 2, 1, 0]
    length = 4
    for i in [0, 1, 2, 3]:
    new_L.append(L[-1] + L[0]) #第一次循环为1
    new_L.append(L[0] + L[1])  #第二次循环为3
    new_L.append(L[1] + L[2])  #第三次循环为3
    new_L.append(L[2] + L[3])  #第四次循环为1
    L = new_L = [1, 3, 3, 1]
....
'''
#其他方法：

'''
def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
通过观察杨辉三角可知，
下一行的每一个元素都依次由本行中每两个相邻元素之和得到，这个方法可以用一个技巧实现，
即：将本行list拷贝出两个副本，将两个副本错1位，然后加在一起。由于错位后，前后各多了一个元素，
所以要在错位后的两个list的前后各加一个[0]来补齐（其实，这个0是理所当然的，是杨辉三角的一部分）。

如图1.1，同一行中前后相邻两个元素相加（这是杨辉三角的构成规则），就相当于两个本行元素错位相加。
而zip方法，就是从这两行中分别取出第i个位置的元素组成元组（这也是添“0”的原因）。
sum()函数正好求出它们的和，进而求出了下一行。
然后又yield函数把这一行“塞入”generator--也就是本例中的triangles()。
'''

'''def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L)-1)] + [1]
'''

n = 0
for t in triangles():
        print(t)
        n = n+1
        if n == 10:
                break


