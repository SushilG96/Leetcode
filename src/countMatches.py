class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        c = 0
        i = 0
        if ruleKey == "type":
            i = 0
        elif ruleKey == "color":
            i = 1
        else:
            i = 2

        for x in items:
            if x[i] == ruleValue:
                c += 1
        return c
