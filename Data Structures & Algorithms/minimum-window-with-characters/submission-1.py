class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if n > m:
            return ""
            
        freq_t = defaultdict(int)
        freq_s = defaultdict(int)
        
        for i in range(n):
            freq_t[t[i]] += 1
            freq_s[s[i]] += 1
            
        # Use >= to check if window CONTAINS t
        def check():
            for letter in t:
                if freq_s[letter] < freq_t[letter]:
                    return False
            return True
            
        start = 0
        end = n - 1
        min_len = m + 1
        answer = ""
        
        # Check the very first window before we start moving!
        if check():
            min_len = n
            answer = s[0:n]

        for i in range(n, len(s)):
            end += 1
            freq_s[s[end]] += 1
            
            # Contract while valid
            while check():
                # Include the end character in the slice
                if min_len > end - start + 1:
                    min_len = end - start + 1
                    answer = s[start:end+1]
                
                # Subtract the CHARACTER, not the integer index
                freq_s[s[start]] -= 1
                # Handle the defaultdict 0-trap we learned earlier!
                if freq_s[s[start]] == 0:
                    del freq_s[s[start]]
                    
                # Move left wall to the RIGHT to shrink
                start += 1
                
        return answer