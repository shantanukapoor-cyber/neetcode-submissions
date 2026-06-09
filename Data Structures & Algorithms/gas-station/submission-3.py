class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        total_sum = 0
        start = 0
        for i in range(n):
            total_sum += gas[i] - cost[i]
            if total_sum < 0:
                start = i + 1
                total_sum = 0
        return start