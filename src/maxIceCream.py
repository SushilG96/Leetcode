class Solution:
    def maxIceCream(self, costs, coins):
        count = 0
        costs.sort()
        for x in range(len(costs)):
            if coins >= costs[x]:
                count += 1
                coins -= costs[x]
            else:
                break
        return count
