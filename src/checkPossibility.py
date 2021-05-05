class Solution:
    def checkPossibility(self, nums):
        violations = 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                violations += 1

                if violations > 1:
                    return False

                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

        return True
