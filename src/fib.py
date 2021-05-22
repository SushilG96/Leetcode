class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        for _ in range(n):
            a, b = a + b, a
        return a


"""
# Solution 2
class Solution:
    def fib(self, n):
        l = [0, 1]
        for x in range(n):
            l.append(l[-1]+l[-2])
        return l[n-1]+l[n-2] if n > 0 else 0
"""
