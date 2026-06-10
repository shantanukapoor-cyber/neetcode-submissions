class Solution:
    def checkValidString(self, s: str) -> bool:
        # f(i) matched by element i
        # if count('(') <= count('*' + ')') 
        # so maintain left bracket count,
        # increment when (
        # decrement when )
        # park sideways when *
        # the parked value has to be used whenever
        # count starts getting negative.
        # if still negative then false.
        # park can be ), or (, or empty.
        lo = 0
        hi = 0
        for symbol in s:
            if symbol == '(':
                lo += 1
                hi += 1
            if symbol == ')':
                lo -= 1
                hi -= 1
            if symbol == '*':
                lo -= 1
                hi += 1
            lo = max(lo, 0)
            if hi < 0:
                return False
        return lo == 0
        
        