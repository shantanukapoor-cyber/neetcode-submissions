from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for x in nums:

            p = bisect_left(tails, x)

            if p == len(tails):
                tails.append(x)
            else:
                tails[p] = x
        return len(tails)