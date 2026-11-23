class ProductOfNumbers:
    def __init__(self):
        self._productsStream = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self._productsStream = [1]
            print(self._productsStream)
            return

        self._productsStream.append(self._productsStream[-1] * num)

    def getProduct(self, k: int) -> int:
        kIdx = len(self._productsStream) - 1 - k
        if kIdx < 0:
            return 0

        return self._productsStream[-1] // self._productsStream[kIdx]
