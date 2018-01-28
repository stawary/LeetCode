#Determine whether an integer is a palindrome. Do this without extra space.

#传统方法，对回文数所有情况进行判断。负数不是回文数，100以内的数除了10都是回文数，超过100的数需要首末位依次判断是否相等。
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x>=0 and x<100 and x!=10:
            return True
        if x>=100:
            x = str(x)
            flag = True
            for i in range(len(x)//2+1):
                if x[i] !=x[len(x)-1-i]:
                    flag=False
            return flag
        
        else:
            return False
