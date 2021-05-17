class Solution:
    def decompressRLElist(self, nums):
        t = []
        for i in range(0, len(nums), 2):
            t.extend(nums[i] * [nums[i + 1]])
        return t
