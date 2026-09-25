class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort()

        min_cost = 0
        i = len(cost) - 1

        while i > 0:
            min_cost += cost[i - 1] + cost[i]
            i -= 3

        if i == 0:
            min_cost += cost[0]

        return min_cost
