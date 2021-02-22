"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
"""
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x:(-len(x),x))

        def helper(sub, whole):
            N, M = len(sub), len(whole)
            i, j = 0, 0

            while j<M and i<N:
                if sub[i]==whole[j]:
                    i+=1
                j+=1
            return  i==N

        out =""
        for w in d:
            if helper(w, s):
                return(w)
        return out
