class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad with 1s to handle boundaries cleanly
        arr = [1] + nums + [1]
        n = len(arr)
        
        memo = {}
        
        def f(i, j):
            # i and j are the boundaries of our current subproblem
            if i > j:
                return 0
                
            if (i, j) in memo:
                return memo[(i, j)]
            
            max_coins = 0
            # Try making every balloon k the LAST one to pop
            for k in range(i, j + 1):
                # Coins from popping k last
                coins = arr[i - 1] * arr[k] * arr[j + 1]
                
                # Add coins from left side and right side
                total = coins + f(i, k - 1) + f(k + 1, j)
                
                max_coins = max(max_coins, total)
            
            memo[(i, j)] = max_coins
            return max_coins
        
        # Solve for the original array, which is between index 1 and n-2
        return f(1, n - 2)