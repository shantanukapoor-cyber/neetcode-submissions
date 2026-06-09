class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # change target to a tuple.
        # operation can be performed 0 or more times.
        # all valid tuples are those which are (i, j, k)
        # i , j, k <= target[0], target[1], target[2]
        # and then since it's a max operation, we can combine all valid tuples.
        # if the final answer is target, it's true else false
        answer = [0, 0, 0]
        for i, j, k in triplets:
            if i <= target[0] and j <= target[1] and k <= target[2]:
                answer[0], answer[1], answer[2] = max(answer[0], i), max(answer[1], j), max(answer[2], k)
        return answer == target