"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

"""
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)[::-1]
        m = 9999

        for x in range(len(arr)-1):
            if arr[x] - arr[x+1] < m:
                m = arr[x] - arr[x+1]
        res = []
        for x in range(len(arr) - 1):
            if arr[x] - arr[x + 1] == m:
                res.append([arr[x+1], arr[x]])
        return(res[::-1])
