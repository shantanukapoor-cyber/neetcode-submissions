class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # take out heap top.
        # take out heap top again.
        # apply the collision protocol.
        # if y - x > 0, push y - x back into heap.
        # do this until length of heap greater than 1.
        heap = [-1* stones[i] for i in range(len(stones))] # O(1)
        print(heap)
        heapq.heapify(heap) # O(N)
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            collision = y - x
            print(collision, heap)
            if -1 * collision > 0:
                heapq.heappush(heap, collision)
        if len(heap) == 1:
            print(heap)
            return -1 * heap[0]
        else:
            return 0
