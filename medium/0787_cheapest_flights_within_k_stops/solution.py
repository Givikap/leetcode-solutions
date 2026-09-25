from collections import deque


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        flightsMap = [[] for _ in range(n)]
        for fr, to, price in flights:
            flightsMap[fr].append((to, price))

        dq = deque([(0, src, 0)])

        pricesMap = [float("inf")] * n
        pricesMap[src] = 0

        while dq:
            stops, fr, price = dq.popleft()

            if stops > k:
                continue

            for to, prc in flightsMap[fr]:
                if pricesMap[to] > price + prc:
                    pricesMap[to] = price + prc
                    dq.append((stops + 1, to, pricesMap[to]))

        return pricesMap[dst] if pricesMap[dst] != float("inf") else -1
