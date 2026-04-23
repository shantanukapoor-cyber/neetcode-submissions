class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force way - for each element check future warmer
        # and  subtract the index.
        result = []
        for i in range(len(temperatures)):
            to_be_inserted = 0
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    to_be_inserted = j-i
                    break
            result.append(to_be_inserted)
        return result