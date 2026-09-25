class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        limitedNums = [nums[0]]

        count = 1

        for i in range(1, len(nums)):
            if limitedNums[-1] == nums[i]:
                if count == k:
                    continue

                count += 1
            else:
                count = 1

            limitedNums.append(nums[i])

        return limitedNums
