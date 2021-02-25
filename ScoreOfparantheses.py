class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res, balance = 0, 0
        for index, par in enumerate(S):
            balance += 1 if par == "(" else -1
            if index and S[index - 1] + par == "()":
                print (balance, index)
                res += 2 ** balance
        return(res)
