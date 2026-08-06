class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            nCopy = n
            digitsProduct = 1

            while nCopy:
                digitsProduct *= nCopy % 10
                nCopy //= 10

            if digitsProduct % t == 0:
                return n
            else:
                n += 1

        return -1
