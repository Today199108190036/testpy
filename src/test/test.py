# -*- coding: UTF-8 -*-
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def testnum():
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if (i != j) and (i != k) and (j != k):
                    print(i,j,k)

#testnum();

# -*- coding: UTF-8 -*-
from itertools import permutations
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def testnum1():
    arr = [1,2,3,4]
    three_numbers = permutations(arr,3)
    for num in three_numbers:
        print(num)

#testnum1()

# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

#题目：输出 9*9 乘法口诀表。
#程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
def testnum2():
    for i in range(1,10):
        print( )
        for j in range(1,i+1):
            print("%d*%d=%d" % (i, j, i*j), end=" ")


testnum2()