class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        rearrangedNums = [0] * len(nums)

        positive = 0
        negative = 1

        for num in nums:
            if num > 0:
                rearrangedNums[positive] = num
                positive += 2
            else:
                rearrangedNums[negative] = num
                negative += 2

        return rearrangedNums
