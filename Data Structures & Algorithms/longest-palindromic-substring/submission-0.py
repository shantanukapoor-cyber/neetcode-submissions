class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        self.start = 0
        self.max_len = 1
        
        def isPalindrome(i, j):
            # Base cases
            if i >= j:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
                
            # Check outer match AND inner palindrome
            memo[(i, j)] = (s[i] == s[j]) and isPalindrome(i + 1, j - 1)
            
            # If it is a palindrome, track the longest one we've seen
            if memo[(i, j)]:
                current_len = j - i + 1
                if current_len > self.max_len:
                    self.max_len = current_len
                    self.start = i
                    
            return memo[(i, j)]
            
        # Check all possible pairs to find the maximum
        for i in range(len(s)):
            for j in range(i, len(s)):
                isPalindrome(i, j)
                
        return s[self.start : self.start + self.max_len]
