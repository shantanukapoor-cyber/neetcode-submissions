class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            pre_req[pre].append(course)
            indegree[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        if not queue:
            return []
        
        order = []
        while queue:
            z = len(queue)
            for _ in range(z):
                eject = queue.popleft()
                order.append(eject)
                for key in pre_req[eject]:
                    indegree[key] -= 1
                    if indegree[key] == 0:
                        queue.append(key)
        if len(order) == numCourses:
            return order
        else:
            return []