class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [1] * (n+1)

        def find(node):
            root = node
            # take the current node as root.
            # if there exist further parents.
            # go upwards till you find start.
            while parent[root] != root:
                root = parent[root]
            
            cur = node
            # now fill this whole chain with root.
            # from cur all the way to it's parents.
            # until we reach begin which is root
            while cur != root:
                # get the original parent
                temp = parent[cur]
                # rewrite current node parent to root
                parent[cur] = root
                # re-point to original 
                cur = temp
            return root
        def union(a, b):
            a = find(a)
            b = find(b)
            # if both part of same set a == b.
            if a == b:
                return False
            if rank[a] > rank[b]:
                parent[b] = a
            elif rank[a] < rank[b]:
                parent[a] = b
            else:
                parent[a] = b
                rank[b] += 1
            return True
        for u, v in edges:
            if not union(u, v):
                return [u, v]




        
            
                
        
        

        
