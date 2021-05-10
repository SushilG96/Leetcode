class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 1 or n == 0 or n == 2:
            return 0
        d = [1] * n
        d[0], d[1] = 0, 0
        i = 2
        while i <= math.sqrt(n):
            if d[i] == 1:
                j = i * i  # i*2
                while j < n:
                    d[j] = 0
                    j = j + i
            i += 1
        return d.count(1)
