class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance for all points from origin
        # sqrt(x**2 + y**2)
        # push to heap and maintain k.
        distance = []
        heapq.heapify(distance)
        for x,y in points:
            span = (x**2 + y**2)**0.5
            heapq.heappush(distance, (-span, x, y))
            while len(distance) > k:
                heapq.heappop(distance)
        return [x[1:] for x in distance]
        
        