class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # k replacements
        # means k allowed different values.
        # what we have to do is first create a running freqency map
        # and expand window till length > max frequency + k.
        # max frequency + k is the length compare with max answer.
        # then shrink window till max frequency + K > length
        # again
        start = 0
        answer = 0
        distinct = defaultdict(int)
        for end in range(len(s)):
            distinct[s[end]] += 1
            while end - start + 1 > max(distinct.values()) + k:
                distinct[s[start]] -= 1
                if distinct[s[start]] == 0:
                    del distinct[s[start]]
                start += 1
            answer = max(answer, end - start + 1)
        return answer