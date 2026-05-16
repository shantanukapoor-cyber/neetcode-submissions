class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if not self.minheap:
            # if min heap is empty push to minheap
            heapq.heappush(self.minheap, num)
        else:
            # if value greater than root move to minheap.
            if num > self.minheap[0]:
                heapq.heappush(self.minheap, num)
            # if otherwise store -ve in minheap becomes maxheap.
            else:
                heapq.heappush(self.maxheap, -num)
            if len(self.minheap) > len(self.maxheap) + 1:
                root = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -root)
            elif len(self.maxheap) > len(self.minheap) + 1:
                root = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -root)
        

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.minheap) < len(self.maxheap):
            return -self.maxheap[0]
        else:
            return (self.minheap[0] + -1*self.maxheap[0]) / 2.0
        
        