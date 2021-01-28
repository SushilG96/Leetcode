def getSmallestString(self, n: int, k: int) -> str:
	c_dict = {i+1: chr(ord('a') + i) for i in range(26)}  # {1:'a', 2:'b' ... 26:'z'}

	lst = ['']*n
	for i in range(n-1, -1, -1): # Reverse fill
		c = min(26, k-i)         # if k-i > 26, character is 'z' else c_dict[k-i]
		lst[i] = c_dict[c]
		k -= c

	return ''.join(lst)

#Sol 2
def getSmallestString(self, n: int, k: int) -> str:
        if n*26 == k:
            return 'z'*n
        k -= n
        nz = k//25
        na = n-nz -1

        return ('a'*na + chr(ord('a')+k%25)+'z'*nz)
