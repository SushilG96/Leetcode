"""
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
"""


class Solution:
    def closeStrings(self, w1, w2):
        return set(w1) == set(w2) and Counter(Counter(w1).values()) == Counter(
            Counter(w2).values()
        )
