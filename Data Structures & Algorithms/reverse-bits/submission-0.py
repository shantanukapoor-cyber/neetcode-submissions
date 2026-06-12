class Solution:
    def reverseBits(self, n: int) -> int:
        # 0 will become 31
        # 1 will become 30
        # i will become n - i - 1
        # To get LSB, we do n % 2
        # to get next n we do n // 2
        # do this till n is 0
        reversed_no = 0
        for i in range(32):
            if n == 0:
                break
            LSB = n % 2
            if LSB == 1:
                reversed_no += 2**(31-i)
            n = n // 2
        return reversed_no
           