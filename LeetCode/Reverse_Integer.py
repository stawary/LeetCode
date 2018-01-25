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
