"""
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for x in bin(n)[2:]:
            if x == '1' :
                count+=1
        return count
