class Solution:
    def addDigits(self, num: int) -> int:        
        def _check(n):
            s = 0
            for x in range(len(str(n))):
                s += int(n[x])
            return (s)
        
        # Input
        n =  str(num)

        # Run the loop until the len on num is 1
        while True:
            if len(n) > 1:
                n = str(_check(n))
            else:
                return(n)
                break

