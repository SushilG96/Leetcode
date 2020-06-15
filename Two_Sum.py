class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        for x in range(len(nums)):
            for y in range(x + 1 ,len(nums)):
                if nums[x] + nums[y] == target:
                    l.append(x)
                    l.append(y)
                    return l
