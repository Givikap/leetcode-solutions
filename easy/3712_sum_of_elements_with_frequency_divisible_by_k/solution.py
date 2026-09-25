from collections import Counter


class Solution:
    def sumDivisibleByK(self, nums: list[int], k: int) -> int:
        return sum(
            num * count
            for num, count in Counter(nums).items()
            if count % k == 0
        )
