"""
A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        dp = [None] * (n - 1)

        for i in range(1, n):
            dp[i - 1] = A[i] - A[i - 1]

        output = 0
        m = 1

        for i in range(1, len(dp)):
            if dp[i] == dp[i - 1]:
                output += m
                m += 1
            else:
                m = 1
        return output
