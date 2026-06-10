class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # convert to intervals.
        # merge intervals.
        # remaining [i, j] intervals
        # they would be the list of integers.
        # now just we have to return the length 
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        
        farthest = 0
        start = 0
        answer = []
        for i, c in enumerate(s):
            farthest = max(farthest, last[c])
            if i == farthest:
                answer.append(i - start + 1)
                start = i + 1
        return answer

            
