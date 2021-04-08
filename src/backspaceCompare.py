def _abc(self, s):
    k = []
    for x in s:
        if x != "#":
            k.append(x)
        else:
            if k:
                k.pop()
    return k


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return _abc(self, S) == _abc(self, T)
