class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bitwise_of_n, res = bin(N)[2:], ""
        for x in bitwise_of_n:
            if x == "1":
                res += "0"
            else:
                res += "1"

        # Convert bin to dec
        return int(res, 2)
