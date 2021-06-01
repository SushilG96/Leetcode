class Solution:
    def convertToBase7(self, n):
        if n == 0:
            return "0"
        s = ""
        sign = "-" if n < 0 else ""
        n = abs(n)
        while abs(n) > 0:
            s += str(n % 7)
            n //= 7
        return sign + s[::-1]
