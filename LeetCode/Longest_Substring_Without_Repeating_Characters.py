#Given a string, find the length of the longest substring without repeating characters.
#Examples:

#Given "abcabcbb", the answer is "abc", which the length is 3.

#Given "bbbbb", the answer is "b", with the length of 1.

#Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, 
#"pwke" is a subsequence and not a substring.
class Solution:
    def lengthOfLongestSubstring(self,s):
        max=0
        if len(s)!=1:
            for i in range(len(s)+1):
                    for j in range(i+1,len(s)+1):
                        if len(s[i:j]) == len(set(s[i:j])): #集合set里没有重复元素
                            if max<j-i:
                                max = j-i
        else:
            max=1
        return max
      
#第一种方法，强力突破 Brute Force。代码里有三段循环，时间复杂度O(n3)。从头开始逐个遍历整个字符串，找到所有的没有重复字符的子字符串，并记录其长度，
#并与已知的最大长度比较，最后得到整个字符串里的最大子字符长度。
