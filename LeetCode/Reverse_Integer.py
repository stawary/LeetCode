'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        if x>0:
            while x>0:
                result = result*10 + x%10  
                x//=10
            if result<=2147483648:
                return result
            else:
                return 0
        else:
            x=-x
            while x>0:
                result = result*10 + x%10
                x//=10
            if result<=2147483648:
                return -result
            else:
                return 0
#自己最开始的代码，其中result<=2147483648是要判断32位整数是否溢出，溢出返回0。python里整除为 // 。

#优化判断x是否大于0的部分
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        s = (x > 0) - (x < 0) #得到正负值
        m = x*s  #m始终为正
        while m > 0:
            result = result*10 + m%10
            m//=10
        if result<=2**31:
            return result*s
        else:
            return 0
        
#上面的方法整数计算的方法，另一种思路是用字符串处理，倒序排列
class Solution:
    def reverse(self, x):
        s = (x > 0) - (x < 0) #得到正负符号
        r = int(str(x*s)[::-1]) #将整型转为字符型并倒序排列再转为整型，list[::-1]为倒序排列
        return s*r * (r < 2**31) #正负号×数值×是否溢出
#此方法最为简练
#学到知识点：
#1、list[::-1]，列表倒序排列
#2、s = (x > 0) - (x < 0)，得到正负号
#3、int32位有符号整数范围为-2^31~2^31,无符号整数范围为0~2^32。
