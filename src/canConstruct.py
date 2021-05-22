class Solution:
    def canConstruct(self, ransomNote, magazine):
        for x in ransomNote:
            if x not in magazine:
                return False
            else:
                magazine = magazine.replace(x, "1", 1)
        return True
