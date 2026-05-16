class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # go through each letter.
        # substring can be length from 1 to len(s).
        # so for each substring we can choose any length
        #  provided isPalindrome = True.
        # once decided substring length, and it's palindrome.
        # we then perform same thing on the reduced substring.
        
        result = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(index, path):
            if index == len(s):          # all characters consumed
                result.append(path[:])
                return
            for end in range(index, len(s)):          # one choice: where does this piece end?
                substring = s[index:end + 1]
                if isPalindrome(substring):           # constraint check at decision point
                    path.append(substring)            # choose
                    backtrack(end + 1, path)           # recurse on remainder
                    path.pop()                         # unchoose

        backtrack(0, [])
        return result
