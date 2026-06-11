class Solution:
    def isHappy(self, n: int) -> bool:
        x = set()
        # n is between 1 and 1000
        # 1000a + 100b + 10c + d
        # abcd
        # a = n // 1000
        # b = n mod 1000 // 100
        # c = n mod 100 // 10
        # d = n mod 10
        x = set()
        while n != 1:
            if n in x:
                return False
            x.add(n)
            n = (n // 1000)**2 + ((n % 1000) // 100)**2 + ((n % 100) // 10 )**2 + ((n % 10) // 1)**2
        return True
