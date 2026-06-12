class Solution:
    def getSum(self, a: int, b: int) -> int:
        if b > 0:
            for i in range(b):
                a += 1
        if b < 0:
            for i in range(abs(b)):
                a -= 1
        return a