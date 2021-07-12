"""
Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
"""


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A = sorted(A)[::-1]
        res = [-1] * len(A)
        c = sorted([(num, i) for i, num in enumerate(B)])[::-1]
        beg, end = 0, len(A) - 1
        for val, ind in c:
            if val < A[beg]:
                res[ind] = A[beg]
                beg += 1
            else:
                res[ind] = A[end]
                end -= 1
        return res
