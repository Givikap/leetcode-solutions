class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        costs = [0] + costs

        oneHopCost = costs[n]
        twoHopCost = float("inf") / 2
        threeHopCost = float("inf") / 2

        for i in range(n - 1, -1, -1):
            threeHopCost, twoHopCost, oneHopCost = (
                twoHopCost,
                oneHopCost,
                costs[i]
                + min(oneHopCost + 1, min(twoHopCost + 4, threeHopCost + 9)),
            )

        return oneHopCost
