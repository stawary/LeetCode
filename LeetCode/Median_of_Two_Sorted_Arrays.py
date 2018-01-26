#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#两个排好序的数组，求这两个数组的中位数。
#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

#Example 1:
#nums1 = [1, 3]
#nums2 = [2]

#The median is 2.0
#Example 2:
#nums1 = [1, 2]
#nums2 = [3, 4]

#The median is (2 + 3)/2 = 2.5
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        for i in range(len(nums2)):
            nums1.append(nums2[i]) #合并nums1和nums2
        nums = sorted(nums1) #排序
        length = len(nums)
        if length%2==1: #长度为奇数
            median = nums[length//2]
        else:  #长度为偶数
            median = (nums[length//2-1]+nums[length//2])/2
        return float(median)
