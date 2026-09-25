class Solution:
    def closestTarget(
        self, words: list[str], target: str, start_index: int
    ) -> int:
        distance = 0
        left = right = start_index

        for _ in range(len(words) // 2 + 1):
            if words[left] == target or words[right] == target:
                return distance

            distance += 1

            left = (left - 1) % len(words)
            right = (right + 1) % len(words)

        return -1
