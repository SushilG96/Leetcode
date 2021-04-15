class Solution:
    def arraySign(self, nums):
        count = 0
        for x in nums:
            if x < 0:
                count += 1
            if x == 0:
                return 0
        return 1 if count % 2 == 0 else -1
