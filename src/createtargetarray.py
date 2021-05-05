class Solution:
    def createTargetArray(self, nums, index):
        res = []
        for x, y in zip(nums, index):
            res.insert(y, x)
        return res
