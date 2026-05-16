class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # possibility is an1 + bn2 + cn3 = target.
        # it will be for [2,5,6,9]
        # first check 0,2,4,6,8 -> check if target - number present.
        # it's N N P N N.
        # so it's the range of not selected, once selected, twice selected, ... selected target // num times
        # what we have to do in backtracking is
        # first have a loop to get all possible values of first element from 0
        # to target // num
        # then we have to run the following checks.
        # generate all possible prefix arrays.
        # compare with target.
        # hand off to next index with index += 1.
        # also, keep only those values in prefix_array that are sum less than target.
        result = []
        def backtrack(i, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0 or i == len(nums):
                return
            # Decision 1: take nums[i], stay at i
            path.append(nums[i])
            backtrack(i, remaining - nums[i], path)
            path.pop()
            # Decision 2: skip nums[i] permanently
            backtrack(i + 1, remaining, path)
        backtrack(0, target, [])
        return result
