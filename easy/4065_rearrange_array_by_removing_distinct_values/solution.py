class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []

        while nums:
            distinct = sorted(set(nums))
            ans.extend(distinct)

            for num in distinct:
                nums.remove(num)

        return ans
