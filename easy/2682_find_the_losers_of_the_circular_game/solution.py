class Solution:
    def circularGameLosers(self, n: int, k: int) -> list[int]:
        losers = list(range(1, n + 1))

        curr = 0
        turn = 1

        while True:
            if not losers[curr]:
                break

            losers[curr] = 0

            curr = (curr + k * turn) % n
            turn += 1

        return [loser for loser in losers if loser]
