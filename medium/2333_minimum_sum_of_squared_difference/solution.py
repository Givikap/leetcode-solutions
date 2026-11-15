from collections import defaultdict


class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        k = k1 + k2

        diffSum = 0
        diffMax = 1
        diffCounter = defaultdict(int)

        for num1, num2 in zip(nums1, nums2):
            diff = abs(num1 - num2)
            diffSum += diff
            diffMax = max(diffMax, diff)
            diffCounter[diff] += 1

        if diffSum <= k:
            return 0

        for diff in range(diffMax, 0, -1):
            if k == 0:
                break

            count = diffCounter[diff]
            if count == 0:
                continue

            if k >= count:
                diffCounter[diff] = 0
                diffCounter[diff - 1] += count
                k -= count
            else:
                diffCounter[diff] -= k
                diffCounter[diff - 1] += k
                k = 0

        return sum(
            diff * diff * diffCounter[diff] for diff in range(diffMax + 1)
        )
