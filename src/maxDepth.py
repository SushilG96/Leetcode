class Solution:
    def maxDepth(self, s):

        currParens = 0
        maxParens = 0

        for x in s:
            if x == "(":
                currParens += 1
            elif x == ")":
                currParens -= 1

            if currParens > maxParens:
                maxParens = currParens

        return maxParens
