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
#并与已知的最大长度比较，最后得到整个字符串里的最大子字符长度。 时间超限！！

#第二种方法，进行优化。可以这样想，如果从头开始第n+1个字符与之前的n个字符串里第一次出现重复，即我们找到第一个最长子字符串长度为n，
#这时候还要从第二、三个字符一个个去遍历往后接着找么？答案是不需要。可以认为前n+1个字符里最长子字符串为n，接下来从第n+2个字符开始找。
class Solution:
    
    def lengthOfLongestSubstring(self,s):
        used = {}
        max_length = start = 0 #start类似C++中的指针，指向子字符串的开头
        for i, c in enumerate(s):
            if c in used and start <= used[c]: #如果遇到与之前相同的字符，将start指针放到这个字符的位置后面重新开始
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1) #没遇到与之前相同的字符，更新最大长度值

            used[c] = i #以字符内容为键，字符的索引为值，构建字典，字典的in方法可以判断值是否存在于字典内。且字典内不允许有重复的值
        return max_length
