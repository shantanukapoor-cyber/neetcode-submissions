class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = len(nums)
        y = len(set(nums))
        if x == y:
            return x!=y
        else:
            return x!=y
         