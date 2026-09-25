class Solution:
    def sumZero(self, n: int) -> list[int]:
        nums = []

        if n % 2 == 1:
            nums.append(0)
            n -= 1

        for num in range(1, n // 2 + 1):
            nums.append(num)
            nums.append(-num)

        return nums
