class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # number : index
        # need to get earliest.
        # for duplicate avoidance we need precheck.
        number = {}

        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in number:
                return [number[complement],i]
            number[nums[i]] = i
        