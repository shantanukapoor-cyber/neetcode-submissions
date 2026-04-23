class MinStack:
    import heapq
    def __init__(self):
        self.container = []
        self.minima = []
        

    def push(self, val: int) -> None:
        self.container.append(val)
        if not self.minima or val <= self.minima[-1]:
            self.minima.append(val)

    def pop(self) -> None:
        x = self.container.pop()
        if self.minima[-1] == x:
            self.minima.pop()

    def top(self) -> int:
        return self.container[-1]

    def getMin(self) -> int:
        return self.minima[-1]
        
