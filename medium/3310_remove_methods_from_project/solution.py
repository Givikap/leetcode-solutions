from collections import deque
from typing import List


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        calledMap = [[] for _ in range(n)]
        callerMap = [[] for _ in range(n)]

        for a, b in invocations:
            calledMap[a].append(b)
            callerMap[b].append(a)

        dq = deque([k])
        suspicious = {k}

        while dq:
            a = dq.popleft()

            for b in calledMap[a]:
                if b not in suspicious:
                    dq.append(b)
                    suspicious.add(b)

        if any(
            i in suspicious and a not in suspicious
            for i in range(n)
            for a in callerMap[i]
        ):
            return list(range(n))

        return [i for i in range(n) if i not in suspicious]
