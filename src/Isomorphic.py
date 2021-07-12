class Solution:
    def isIsomorphic(self, s, t):
        return [s.index(ch) for ch in s] == [t.index(ch) for ch in t]
