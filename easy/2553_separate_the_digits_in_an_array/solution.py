class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        digits = []

        for num_str in map(str, nums):
            for digit in num_str:
                digits.append(ord(digit) - 48)

        return digits
