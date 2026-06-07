class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # from any position, we can either have a match or not.
        # at position i in word1 and j in word2.
        # word1[i] == word2[j]
        # then i->i+1 and j->j+1
        # if word1[i] != word2[j]
        # then if we insert a new character.
        # i->i and j->j+1
        # if we delete current charater.
        # i-> i+1 and j->j
        # if we replace a character
        # i-> i+1 and j->j+1
        # f(i, j) = minimum of each transition.
        # if we reach len(word2) -> return len(word1) - i prune all remaining letters
        # if we reach len(word1) -> return len(word2) - j insert all remaining letters

        memo = {}

        def minways(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = minways(i+1, j+1)
            else:
                memo[(i, j)] = min(1 + minways(i, j+1), 1 + minways(i+1, j), 1 + minways(i+1, j+1))
            return memo[(i, j)]
        
        return minways(0, 0)