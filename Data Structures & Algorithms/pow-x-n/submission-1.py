class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n > 0:
            while n > 0:
                result *= x
                n -= 1
        if n < 0:
            while n < 0:
                result = result / x
                n += 1
        return result