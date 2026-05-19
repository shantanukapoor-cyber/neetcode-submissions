class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((t, v))
        # directed edge from u to v for time t.
        heap = [(0, k)]
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        while heap:
            cost, u = heapq.heappop(heap)
            if cost > dist[u]:
                continue
            for edge_cost, v in adj_list[u]:
                new_cost = cost + edge_cost
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(heap, (new_cost, v))
        max_time = -1
        for key in dist:
            if dist[key] == float('inf'):
                return -1
            max_time = max(max_time, dist[key])
        return max_time