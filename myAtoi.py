class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        num = 0

        if not s:
            return 0
        s = s.strip()

        # sign
        if s and s[0] in "+-":
            sign = 1 if s[0] == "+" else -1
            s = s[1:]
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            else:
                break
        res = num * sign
        if res >= (2 ** 31):
            return (2 ** 31) - 1
        elif res < -(2 ** 31):
            return -(2 ** 31)

        return res
