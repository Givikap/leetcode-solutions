from collections import defaultdict


class Solution:
    def twoOutOfThree(
        self, nums1: list[int], nums2: list[int], nums3: list[int]
    ) -> list[int]:
        numsCounter = defaultdict(lambda: [0] * 3)

        for i, nums in enumerate([nums1, nums2, nums3]):
            for num in nums:
                numsCounter[num][i] += 1

        nums = []

        for num, counter in numsCounter.items():
            if counter.count(0) <= 1:
                nums.append(num)

        return nums
