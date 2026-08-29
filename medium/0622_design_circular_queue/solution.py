class MyCircularQueue:
    def __init__(self, k: int):
        self.buffer = [0] * k

        self.size = 0
        self.capacity = k

        self.front = 0
        self.back = k - 1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.back = (self.back + 1) % self.capacity
        self.buffer[self.back] = value
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        return True

    def Front(self) -> int:
        return self.buffer[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.buffer[self.back] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
