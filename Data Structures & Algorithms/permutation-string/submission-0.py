class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 is permuted to s2
        # letters are same.
        # also, length must be same for the len(s1) = len(window)
        freq_s1 = defaultdict(int)
        freq_s2 = defaultdict(int)
        start = 0
        n = len(s1)
        end = n-1
        if len(s2) < n:
            return False
        for index in range(n):
            freq_s1[s1[index]] += 1
            freq_s2[s2[index]] += 1
        if freq_s1 == freq_s2:
            return True
        for j in range(n,len(s2)):
            # Move the window
            freq_s2[s2[start]] -= 1
            if freq_s2[s2[start]] == 0:
                del freq_s2[s2[start]]   
            start += 1
            end += 1
            freq_s2[s2[end]] += 1
            if freq_s1 == freq_s2:
                return True    
        return False

        
        

        
