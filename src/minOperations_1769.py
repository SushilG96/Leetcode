# 1769. Minimum Number of Operations to Move All Balls to Each Box
class Solution:
    def minOperations(self, boxes):
        ones = [x for x in range(len(boxes)) if boxes[x] == "1"]
        # print(ones)
        res = []

        for i in range(len(boxes)):
            tmp = 0
            for k in ones:
                tmp += abs(k - i)
            res.append(tmp)

        return res
