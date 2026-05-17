class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prepare indegree list. [root, indree]
        pre_req = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            pre_req[pre].append(course)
            indegree[course] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        visited = 0
        while queue:
            z = len(queue)
            for _ in range(z):
                eject = queue.popleft()
                visited += 1
                for key in pre_req[eject]:
                    indegree[key] -= 1
                    if indegree[key] == 0:
                        queue.append(key)
        return numCourses == visited

        

