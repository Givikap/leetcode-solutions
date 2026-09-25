class Solution:
    def findRelativeRanks(self, scores: list[int]) -> list[str]:
        podium = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        ranked_scores = sorted(
            enumerate(scores), key=lambda x: x[1], reverse=True
        )
        ranks = [""] * len(scores)

        for rank, (i, _) in enumerate(ranked_scores, start=1):
            ranks[i] = podium[rank - 1] if rank < 4 else str(rank)

        return ranks
