from typing import Counter


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        numsCounter = dict(sorted(Counter(nums).items()))

        ans = []

        while numsCounter:
            toAdd = []
            toRemove = []

            for num, count in numsCounter.items():
                numsCounter[num] -= 1

                toAdd.append(num)
                if count == 1:
                    toRemove.append(num)

            ans.extend(toAdd)
            for num in toRemove:
                numsCounter.pop(num)

        return ans
