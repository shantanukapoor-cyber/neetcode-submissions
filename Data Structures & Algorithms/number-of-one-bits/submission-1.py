class Solution:
    def hammingWeight(self, n: int) -> int:
        M = 2**32
        count_of_one = 0
        while M > 0:
            if n >= M:
                count_of_one += n // M
            n = n % M
            M = M // 2
        return count_of_one