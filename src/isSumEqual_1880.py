# 1880. Check if Word Equals Summation of Two Words
def to_sum(word):
    k = ""
    for char in word:
        k += str(ord(char) - 97)
    return int(k)


class Solution:
    def isSumEqual(self, firstWord, secondWord, targetWord):
        return to_sum(firstWord) + to_sum(secondWord) == to_sum(targetWord)
