from itertools import permutations


class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        return len(
            set(
                perm
                for perm in permutations(digits, 3)
                if perm[0] != 0 and perm[-1] % 2 == 0
            )
        )
