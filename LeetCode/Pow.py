#Implement pow(x, n).
#计算x的n次方
#Example 1:

#Input: 2.00000, 10
#Output: 1024.00000
#Example 2:

#Input: 2.10000, 3
#Output: 9.26100

#第一种传统方法，逐个相乘，需考虑n<0的情况，x=1/x。
class Solution:
    def myPow(self, x, n):
        ans = 1
        if n<0:
            x=1/x
        
        for i in range(abs(n)):
            ans = ans*x
        return ans
