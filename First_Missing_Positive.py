class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        new_list = sorted(list(set([x for x in nums if x > 0])))
        if len(new_list) >= 1 and new_list[0] > 0:
            for x in range(1, new_list[-1] + 1):
                if x != new_list[x - 1]:
                    return x
            return new_list[-1] + 1
        elif len(new_list) == 1:
            if new_list[0] == 0:
                return 0
        return 1
