class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            middle = left + (right - left)//2
            if nums[middle] < nums[right]: 
                # right half is sorted.
                right = middle
            elif nums[middle] > nums[right]:
                left = middle + 1
        return nums[left]
        