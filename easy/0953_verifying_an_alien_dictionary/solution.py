class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}

        for word1, word2 in zip(words, words[1:]):
            for c1, c2 in zip(word1, word2):
                if order_map[c1] < order_map[c2]:
                    break
                elif order_map[c1] > order_map[c2]:
                    return False
            else:
                if len(word1) > len(word2):
                    return False

        return True
