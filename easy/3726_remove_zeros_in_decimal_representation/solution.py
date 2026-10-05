class Solution:
    def removeZeros(self, n: int) -> int:
        m = 0
        mul = 1

        while n:
            digit = n % 10
            n //= 10

            if digit:
                m += digit * mul
                mul *= 10

        return m
