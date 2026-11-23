class ProductOfNumbers:
    def __init__(self):
        self._products = []

    def add(self, num: int) -> None:
        if num != 1:
            for i in range(len(self._products)):
                self._products[i] *= num

        self._products.append(num)

    def getProduct(self, k: int) -> int:
        return self._products[-k]
