class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        obstacles_set = set(map(tuple, obstacles))

        x = y = 0
        direction = 0

        max_distance = 0

        for command in commands:
            if command == -1:
                direction += 90
            elif command == -2:
                direction -= 90
            else:
                direction %= 360
                dx = dy = 0

                if direction == 0:
                    dy = 1
                elif direction == 90:
                    dx = 1
                elif direction == 180:
                    dy = -1
                elif direction == 270:
                    dx = -1

                for _ in range(command):
                    if (x + dx, y + dy) in obstacles_set:
                        break

                    x += dx
                    y += dy

                max_distance = max(max_distance, x**2 + y**2)

        return max_distance
