class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct_nums = set(nums)
        max_length = 0
        for value in distinct_nums:
            length = 1
            if value-1 not in distinct_nums:
                while  value+1 in distinct_nums:
                    length += 1
                    value += 1
            max_length = max(max_length, length)
        return max_length

    

        