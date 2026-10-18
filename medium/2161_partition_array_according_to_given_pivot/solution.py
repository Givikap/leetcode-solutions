class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        lesser = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                lesser.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)

        return lesser + equal + greater
