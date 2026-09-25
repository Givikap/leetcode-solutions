class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in reversed(range(len(digits))):
            digits[i] += 1

            if digits[i] == 10:
                digits[i] = 0

                if i == 0:
                    return [1] + digits

                continue

            return digits
