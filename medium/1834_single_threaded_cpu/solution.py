import heapq
from collections import deque


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        tasks = deque(sorted([(*task, i) for i, task in enumerate(tasks)]))

        time = tasks[0][0]
        available = []

        order = []

        while tasks or available:
            if not available and time < tasks[0][0]:
                time = tasks[0][0]

            while tasks and tasks[0][0] <= time:
                heapq.heappush(available, tasks.popleft()[1:])

            if available:
                processing_time, i = heapq.heappop(available)

                time += processing_time
                order.append(i)

        return order
