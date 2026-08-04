from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        n = len(nums)

        jumpledPairs = []

        for i in range(n):
            num = nums[i]
            jumbledNum = 0

            if num == 0:
                jumbledNum = mapping[0]
            else:
                mul = 1

                while num:
                    jumbledNum += mapping[num % 10] * mul
                    num //= 10
                    mul *= 10

            jumpledPairs.append((jumbledNum, i))

        jumpledPairs.sort()

        jumpledNums = []
        for i in range(n):
            jumpledNums.append(nums[jumpledPairs[i][1]])

        return jumpledNums
