class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Track global max, current running max, and current running min
        global_max = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            num = nums[i]
            
            # If the current number is negative, cur_max and cur_min swap roles
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
            
            # Decide whether to add to the existing subarray or start a new one
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)
            
            # Update the highest product found so far
            global_max = max(global_max, cur_max)
            
        return global_max
