class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        shuffled_nums = []

        for x, y in zip(range(n), range(n, 2 * n)):
            shuffled_nums.extend((nums[x], nums[y]))

        return shuffled_nums
