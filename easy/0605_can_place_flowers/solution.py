class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed_len = len(flowerbed)

        i = 0
        while n and i < flowerbed_len:
            if flowerbed[i] == 0:
                if (i - 1 == -1 or flowerbed[i - 1] == 0) and (
                    i + 1 == flowerbed_len or flowerbed[i + 1] == 0
                ):
                    flowerbed[i] = 1
                    n -= 1

                    i += 1

            i += 1

        return n == 0
