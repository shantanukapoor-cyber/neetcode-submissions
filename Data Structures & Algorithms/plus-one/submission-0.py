class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        M = len(digits)
        i = 0
        n = 0
        while i < len(digits):
            n += digits[i]*10**(M-1)
            i += 1
            M -= 1
        n += 1
        return [int(x) for x in str(n)]