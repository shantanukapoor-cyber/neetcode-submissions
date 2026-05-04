class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        frequency = set()
        for num in nums:
            if num in frequency:
                return num
            frequency.add(num)
        return -1