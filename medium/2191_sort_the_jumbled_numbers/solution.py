class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def mapJumbled(num: int):
            if num == 0:
                return mapping[0]
            else:
                mul = 1
                jumbledNum = 0

                while num:
                    jumbledNum += mapping[num % 10] * mul
                    num //= 10
                    mul *= 10

                return jumbledNum

        nums.sort(key=lambda num: mapJumbled(num))

        return nums
