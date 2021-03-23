class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy = prices[0]
        #sell = 0
        #profit = 0
        #flag = True
        #if prices == sorted(prices):
        #    return (prices[-1] - prices[0])
        # prices.append(0)
        # for i in range(1, len(prices)):
        #     if prices[i] <= buy:
        #         buy = prices[i]
        #         flag = True
        #         print("In for buy",buy)
        #     else:
        #         if flag and prices[i] > prices[i+1]:
        #             sell = prices[i]
        #             profit += sell - buy
        #             print("sell {} --- buy {}".format(buy, sell), profit)
        #             buy = prices[i+1]
        #             flag = False
        # return(profit)
        if prices is None or len(prices) == 0:
            return 0
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]

        return profit

