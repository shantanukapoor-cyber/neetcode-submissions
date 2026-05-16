class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for each number we can either select it or ignore it.
        # it can be ignore ignore ignore.
        # take ignore ignore, ignoe take ignore, ignore ignore take
        # tit, tti, itt, ttt.
        answer = []

        def backtrack(index, subset):
            if index == len(nums):
                answer.append(list(subset))
                return
            # selection
            subset.append(nums[index])
            backtrack(index+1, subset)
            subset.pop()
            backtrack(index+1, subset)
            
        backtrack(0,[])
        return answer


