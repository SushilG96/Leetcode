class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations, combinations

        res = [[]]
        for i in range(len(nums)):
            oc = combinations(nums, i + 1)
            for c in oc:
                res.append(list(c))
        return res
