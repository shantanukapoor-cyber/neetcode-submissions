class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = defaultdict(int)
        for i in range(n):
            for j in range(n):
                dist[(i, j)] = float('inf')
        heap = [(grid[0][0],(0,0))]
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        dist[(0,0)] = grid[0][0]
        while heap:
            cost, vertex = heapq.heappop(heap)
            if cost > dist[vertex]:
                continue
            r, c = vertex
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_cost = max(cost,grid[nr][nc])
                    if new_cost < dist[(nr, nc)]:
                        dist[(nr, nc)] = new_cost
                        heapq.heappush(heap, (new_cost, (nr, nc)))
        return dist[(n-1, n-1)]

