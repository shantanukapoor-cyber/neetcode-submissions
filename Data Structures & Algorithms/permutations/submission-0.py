class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index):
            # if we reach the end send the list to result.
            if index == len(nums):
                result.append(nums[:])
                return
            # for each term with and after index consider at index.
            for i in range(index, len(nums)):
                # choose one of the future value
                nums[i], nums[index] = nums[index], nums[i]
                # go to next position - it will store in result
                backtrack(index + 1)
                # undo the changes back to account  for next case
                nums[index], nums[i]  = nums[i], nums[index]
        backtrack(0)
        return result

            
            