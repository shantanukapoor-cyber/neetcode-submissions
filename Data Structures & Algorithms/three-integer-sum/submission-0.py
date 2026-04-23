class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        intermediate = set()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        order = sorted((nums[i],nums[j],nums[k]))
                        intermediate.add(tuple(order))
        answer = []
        for tuple_values in intermediate:
            answer.append(list(tuple_values))

        return answer
