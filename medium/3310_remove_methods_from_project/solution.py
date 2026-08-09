from collections import deque
from typing import List


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        calledMap = [[] for _ in range(n)]

        for a, b in invocations:
            calledMap[a].append(b)

        suspicious = [False] * n
        suspicious[k] = True

        dq = deque([k])
        while dq:
            a = dq.popleft()

            for b in calledMap[a]:
                if not suspicious[b]:
                    suspicious[b] = True
                    dq.append(b)

        for a, b in invocations:
            if not suspicious[a] and suspicious[b]:
                return list(range(n))

        return [a for a in range(n) if not suspicious[a]]
