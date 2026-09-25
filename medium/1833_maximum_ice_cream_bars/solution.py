class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costsCounter = [0] * (max(costs) + 1)
        for cost in costs:
            costsCounter[cost] += 1

        iceCreamCount = 0

        for cost in range(1, len(costsCounter)):
            count = costsCounter[cost]
            if not count:
                continue

            iceCreamsCost = cost * count
            if coins >= iceCreamsCost:
                coins -= iceCreamsCost
                iceCreamCount += count
            else:
                while coins >= cost:
                    coins -= cost
                    iceCreamCount += 1

        return iceCreamCount
