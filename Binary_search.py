class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        h = len(nums) - 1
        mid = 0

        while l <= h:
            mid = (l + h) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                return mid
        return -1
