class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitsSum = 0
        digitsProduct = 1

        nCopy = n

        while nCopy:
            digit = nCopy % 10
            nCopy //= 10

            digitsSum += digit
            digitsProduct *= digit

        return n % (digitsSum + digitsProduct) == 0
