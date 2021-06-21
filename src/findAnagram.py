class Solution:
    def findAnagrams(self, s, p):
        res = []
        l_p = len(p)
        p = sorted(p)
        # print(p)
        for x in range(len(s) - l_p + 1):
            k = sorted(s[x: x + l_p])
            if k == p:
                res.append(x)
        return res
