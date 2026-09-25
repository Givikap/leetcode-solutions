from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = [nums[0]]

        for num in nums:
            if num > tails[-1]:
                tails.append(num)
            elif num < tails[-1]:
                tails[bisect_left(tails, num)] = num

        return len(tails)
