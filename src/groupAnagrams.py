def groupAnagrams(self, strs):
    r = sorted([["".join(sorted(i)), i] for i in strs[:]])
    k = []
    t = []
    for x in r:
        if x[0] not in t:
            t.append(x[0])
            k.append([x[1]])
        else:
            k[-1].extend([x[1]])
    return k
