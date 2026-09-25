class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        not_seen = list(range(len(nums) + 1))

        for num in nums:
            if not_seen[num]:
                not_seen[num] = 0
            else:
                duplicate = num

        mismatch = next(num for num in not_seen if num)

        return [duplicate, mismatch]
