class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k):
            total = 0
            for pile in piles:
                factor = pile // k
                if pile % k != 0:
                    total += factor + 1
                else:
                    total += factor
                # total += (pile + k - 1) // k
                if total > h:
                    return False
            return True
        
        minima = 1
        maxima = 10**9
        while minima <= maxima:
            middle = minima + (maxima - minima)//2
            if eat(middle):
                maxima = middle - 1
            else:
                minima = middle + 1
        return minima