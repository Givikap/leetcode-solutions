import heapq
from collections import deque


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(tasks)

        serverHeap = [(server, i) for i, server in enumerate(servers)]
        taskQueue = deque([])
        jobHeap = []

        heapq.heapify(serverHeap)

        ans = [-1] * n

        t = 0
        while t < n or taskQueue:
            while jobHeap and jobHeap[0][0] <= t:
                _, i = heapq.heappop(jobHeap)
                heapq.heappush(serverHeap, (servers[i], i))

            if t < n:
                taskQueue.append(t)

            while serverHeap and taskQueue:
                _, i = heapq.heappop(serverHeap)
                j = taskQueue.popleft()

                heapq.heappush(jobHeap, (t + tasks[j], i))
                ans[j] = i

            if t >= n - 1 and not serverHeap and taskQueue and jobHeap:
                t = jobHeap[0][0]
            else:
                t += 1

        return ans
