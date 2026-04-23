class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        from collections import defaultdict
        mapping = defaultdict(int)

        for i in range(len(numbers)):
            complement = target-numbers[i]
            if complement in mapping:
                return [mapping[complement], i+1]
            mapping[numbers[i]] = i+1