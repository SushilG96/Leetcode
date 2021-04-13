def encode(p):
    p_encode = {}
    tmp = 0
    s = ""
    for x in p:
        if x not in p_encode:
            p_encode[x] = tmp
            s += str(tmp)
            tmp += 1
        else:
            s += str(p_encode[x])
    return s
class Solution:
    def findAndReplacePattern(self, words, pattern):
        pattern = encode(pattern)
        return ([x for x in words if encode(x) == pattern])

