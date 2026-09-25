class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix_sums = [0]

        for num in nums:
            self.prefix_sums.append(self.prefix_sums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]
