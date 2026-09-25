class Robot:
    directions = ["East", "North", "West", "South"]

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.perimeter = 2 * (width + height) - 4

        self.x = 0
        self.y = 0
        self.direction = 0

    def step(self, num: int) -> None:
        if self.perimeter == 0:
            return

        num %= self.perimeter
        if num == 0:
            num = self.perimeter

        while num > 0:
            if self.direction == 0:
                distance = (self.width - 1) - self.x
                if num <= distance:
                    self.x += num
                    return
                self.x = self.width - 1
            elif self.direction == 1:
                distance = (self.height - 1) - self.y
                if num <= distance:
                    self.y += num
                    return
                self.y = self.height - 1
            elif self.direction == 2:
                distance = self.x
                if num <= distance:
                    self.x -= num
                    return
                self.x = 0
            else:
                distance = self.y
                if num <= distance:
                    self.y -= num
                    return
                self.y = 0

            num -= distance
            self.direction = (self.direction + 1) % 4

    def getPos(self) -> list[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.directions[self.direction]
