class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(index, remaining, parts):
            if remaining == 0:
                if tuple(parts[:]) not in result:
                    result.append(list(parts))
                return
            # prune condition
            # throw out if sum > target or all elements done.
            if index == len(candidates) or remaining < 0:
                return
            for i in range(index, len(candidates)):
                if candidates[i] == candidates[i-1] and i > index:
                    continue
                if remaining < candidates[i]:
                    break
                
                parts.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], parts)
                # or skip current element
                parts.pop()
        backtrack(0, target, [])
        return result