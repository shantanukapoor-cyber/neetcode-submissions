class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # take out heap top.
        # take out heap top again.
        # apply the collision protocol.
        # if y - x > 0, push y - x back into heap.
        # do this until length of heap greater than 1.
        heap = [-1 * stones[i] for i in range(len(stones))] # O(1)
        heapq.heapify(heap) # O(N)
        while len(heap) > 1: # O(N)
            y = heapq.heappop(heap) # O(logN)
            x = heapq.heappop(heap) # O(logN)
            collision = y - x
            if -1 * collision > 0:
                heapq.heappush(heap, collision) # O(logN)
        heap.append(0)
        return abs(heap[0])
        # O(NlogN)
