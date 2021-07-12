from itertools import combinations


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        comb = combinations([x for x in range(1, 10)], k)
        combination = [list(x) for x in list(comb) if sum(x) == n]
        return combination
