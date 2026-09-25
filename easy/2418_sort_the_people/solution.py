class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [
            name
            for _, name in sorted(
                (-height, names[i]) for i, height in enumerate(heights)
            )
        ]
