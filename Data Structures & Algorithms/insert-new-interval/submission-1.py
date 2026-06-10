class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if I1 and newInt.
        # I1[1] > newInt[0] or I[0] < newInt[1] then merge to min(I1[0], newInt[0])
        # and max(I1[1], newInt[0])
        # intervals in ascending order,
        # that means first we check the ending interval
        # and append only if all merges done or non overlapping.
        tx, ty = newInterval
        resultAdded = 0
        result = []
        for a, b in intervals:
            if a <= tx <= b or a <= ty <= b:
                tx = min(a, tx)
                ty = max(b, ty)
            if b < tx:
                result.append([a, b])
            if ty < a:
                if resultAdded == 0:
                    result.append([tx, ty])
                    resultAdded = 1
                result.append([a, b])
        if resultAdded == 0:
            result.append([tx, ty])
            resultAdded = 1
        return result

            
