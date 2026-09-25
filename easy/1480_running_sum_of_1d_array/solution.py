class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running_sum = []
        curr_sum = 0

        for num in nums:
            curr_sum += num
            running_sum.append(curr_sum)

        return running_sum
