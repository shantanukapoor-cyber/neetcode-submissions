class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks).values()
        f_max = max(counts)
        n_max = list(counts).count(f_max)
        
        # Applying the geometric formula
        formula_result = (f_max - 1) * (n + 1) + n_max
        
        # Return the larger of the formula or the raw task count
        return max(len(tasks), formula_result)
