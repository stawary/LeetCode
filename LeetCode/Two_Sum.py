#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:
#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result =[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target ):
                    result.append(i)
                    result.append(j)
        return result
      
#时间复杂度 O(n2)，循环遍历2次列表元素，找到可以配对的值。最蛮力的方法。
#python的此种方法如果数量级很大，会时间超限。

#另一种算法，使用哈希算法，python中即dict

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            x = nums[i]
            if target-x in dic:
                return [dic[target-x], i]
            dic[x] = i

#时间复杂度O(n)，只遍历一次列表。利用dict的键值对，num:index，依次写入到dict里。然后借助dict的in操作符，
#如果键存在于字典里，返回True，用以判断是否存在target-x。如果存在，返回键所对应的值，即索引。
