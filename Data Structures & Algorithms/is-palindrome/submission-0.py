class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        pattern = r'[A-Za-z0-9]+'
        result = re.findall(pattern, s)
        result = "".join(result)
        l = 0
        r = len(result)-1
        while l < r:
            if result[l].lower() != result[r].lower():
                return False
            else:
                l += 1
                r -= 1
        
        return True