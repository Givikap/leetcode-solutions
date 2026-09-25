class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        min_cost = [0] * (len(cost) - 1) + [cost[-1], 0]

        for i in range(len(cost) - 2, -1, -1):
            min_cost[i] = cost[i] + min(min_cost[i + 1], min_cost[i + 2])

        return min(min_cost[0], min_cost[1])
