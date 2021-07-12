"""
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = arr.count(0)
        to_ins = []
        for x in range(len(arr)):
            if arr[x] == 0:
                to_ins.append(x)
        for x in range(count):
            arr.insert(to_ins[x] + x, 0)
            arr.pop()
