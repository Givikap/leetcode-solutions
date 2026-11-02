class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        sortedNums = [0] * len(nums)

        evenIdx = 0
        oddIdx = 1

        for num in nums:
            if num % 2 == 0:
                sortedNums[evenIdx] = num
                evenIdx += 2
            else:
                sortedNums[oddIdx] = num
                oddIdx += 2

        return sortedNums
