class Solution:
    def maxProduct(self, words):
        m = 0
        for x in words:
            for i in words:
                if not set(x)&set(i):
                    k =len(x) * len(i)
                    if k > m:
                        m = k
        return(m)
