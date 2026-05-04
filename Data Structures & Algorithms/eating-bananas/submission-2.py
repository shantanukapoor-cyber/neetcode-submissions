class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k):
            total = 0
            for pile in piles:
                total += (pile + k - 1) // k
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