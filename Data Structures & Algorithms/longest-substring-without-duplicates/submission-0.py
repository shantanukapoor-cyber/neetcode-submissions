class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        freq = set()
        answer = 0
        
        for end in range(len(s)):
            # While the character is a duplicate, 
            # shrink the window from the left
            while s[end] in freq:
                freq.remove(s[start])
                start += 1
            
            # Now it's safe to add the character
            freq.add(s[end])
            
            # Update the maximum length found
            answer = max(answer, end - start + 1)
            
        return answer
