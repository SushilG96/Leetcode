"""
Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
"""
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for x in s:
            if x in "({[":
                l.append(x)
            else:
                if x == ")":
                    if l and l[-1] == "(":
                        l.pop()
                    else:
                        return False
                if x == "}":
                    if l and l[-1] == "{":
                        l.pop()
                    else:
                        return False
                if x == "]":
                    if l and l[-1] == "[":
                        l.pop()
                    else:
                        return False
        return (False if l else True)
