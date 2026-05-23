class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        tickets.sort(reverse=True)
        for u, v in tickets:
            adj_list[u].append(v)

        result = []
        def dfs(node):
            while adj_list[node]:
                y = adj_list[node].pop()
                dfs(y)
            result.append(node)
        dfs('JFK')
        return result[::-1]


        