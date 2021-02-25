"""
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        tmp = sorted(nums)

        start, end = -1 ,-1
        for i, x in enumerate(range(len(tmp)-1, -1 , -1)):
            if start == -1 and nums[i] != tmp[i]:
                print("here")
                start = i
            if end == -1 and nums[x] != tmp[x]:
                end = x
        return(len(tmp[start:end+1]))
