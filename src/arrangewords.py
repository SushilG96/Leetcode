class Solution:
    def arrangeWords(self, text: str) -> str:
        test = text.split(" ")
        test.sort(key=len)
        res = []
        for i, x in enumerate(test):
            if i == 0:
                if x[0].islower():
                    x = x[0].upper() + x[1:]
                res.append(x)
            else:
                if x[0].isupper():
                    x = x[0].lower() + x[1:]
                res.append(x)
        return " ".join(res)
