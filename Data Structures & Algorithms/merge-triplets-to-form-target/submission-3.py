class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        seen = [False]*3
        tx, ty, tz = target[0], target[1], target[2]
        for a,b,c in triplets:
            if a<=tx and b<=ty and c<=tz:
                if a==tx: seen[0]=True
                if b==ty: seen[1]=True
                if c==tz: seen[2]=True

        return all(seen)