class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        winners = set()
        one_loss = set()
        many_losses = set()

        for winner, loser in matches:
            winners.add(winner)

            if loser not in one_loss:
                one_loss.add(loser)
            else:
                many_losses.add(loser)

        return [
            sorted(winners - one_loss - many_losses),
            sorted(one_loss - many_losses),
        ]
