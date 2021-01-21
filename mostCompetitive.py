class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        l = []

        # m elemnts need to be there
        m = len(nums) - k

        for x in nums:
            while l and l[-1] > x and m > 0:
                m -= 1
                l.pop()
            l.append(x)
        return l[:k]
