class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        n = len(s)
        reverse_map = defaultdict(list)
        distinct_word = set()
        for word in wordDict:
            index = len(word)
            reverse_map[index].append(word)
            distinct_word.add(word)

        def solve(index):
            if index == n:
                return True
            if index > n:
                return False
            if index in memo:
                return memo[index]
            for transition in reverse_map.keys():
                substring = s[index:index+transition]
                if substring in distinct_word:
                    if solve(index+transition):
                        memo[index] = True
                        return True
            memo[index] = False
            return False
        
        return solve(0)
