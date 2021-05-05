class Solution:
    def maxScore(self, cardPoints, k):
        left = [0] * (k + 1)
        right = [0] * (k + 1)

        rev_ = cardPoints[::-1]
        for x in range(0, k):
            left[x + 1] = cardPoints[x] + left[x]
            right[x + 1] = rev_[x] + right[x]

        sum = 0
        right = right[::-1]
        for x, y in zip(left, right):
            cur = x + y
            if cur > sum:
                sum = cur
        return sum
