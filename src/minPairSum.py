class Solution:
    def minPairSum(self, nums):
        nums.sort()
        return max([nums[x] + nums[-x - 1] for x in range(len(nums) // 2)])
