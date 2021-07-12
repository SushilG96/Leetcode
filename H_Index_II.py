class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for x in range(len(citations), 0, -1):
            print(citations[x - 1], x)
            if citations[x - 1] >= x:
                return x
        return 0
