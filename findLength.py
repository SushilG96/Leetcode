# chr() takes only one integer and return its Character value,
"""
>>> ord("a")
97
>>> chr(97)
'a'
"""


class Solution:
    def findLength(self, nums1, nums2):

        # Fetch the Ascii value for each elements and store them as string
        nums1 = "".join([chr(x) for x in nums1])
        nums2 = "".join([chr(x) for x in nums2])

        bi, sm = "", ""
        if len(nums1) < len(nums2):
            bi, sm = nums2, nums1
        else:
            bi, sm = nums1, nums2

        n, i, j, res = len(sm), 0, 1, 0

        while j <= n:
            if sm[i:j] in bi:
                tmp = len(sm[i:j])
                if tmp > res:
                    res = tmp
                j += 1
            else:
                i += 1
                j += 1
        return res
