class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 1. Create the frequency map
        freq = Counter(nums)
        # 2. Extract unique keys to maintain an ordered pass
        unique_keys = list(freq.keys())
        def backtrack(index, path):
            if index == len(unique_keys):
                result.append(path[:])    # every leaf is valid
                return
            value = unique_keys[index]
            count = freq[value]
            for c in range(count + 1):
                for _ in range(c):
                    path.append(value)
                backtrack(index + 1, path)
                for _ in range(c):
                    path.pop()

        backtrack(0, [])
        return result

