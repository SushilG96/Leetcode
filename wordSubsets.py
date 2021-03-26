class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        d ={}
        for x in B:
            for b in x:
                if b in d:
                    d[b] = max(x.count(b), d[b])
                else:
                    d[b] = x.count(b)
        tmp = []
        for a in A:
            d1 = d.copy()
            for i in a:
                if i in d1 :
                    d1[i] -= 1
                    if d1[i]  < 0:
                        d1[i] = 0

            if sum(list(d1.values())) == 0:
                tmp.append(a)
        return tmp
