class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # f(i) = start from index i.
        # f([i + 1] % n) = f(i) + gas[i] - cost[i]
        # f(start) = 0.
        # if we reach [i+1]%n == start
        # that means start should be return.
        n = len(gas)

        def rotate(i):
            start = i
            step_count = 0
            ability = gas[i] - cost[i]
            i = (i+1) % n
            while step_count < n and ability >= 0:
                ability = ability + gas[i] - cost[i]
                i = (i + 1) % n
                step_count += 1
            if step_count == n:
                return start
            else:
                return -1

        for i in range(n):
            end = rotate(i)
            if end == i:
                return end
        return -1