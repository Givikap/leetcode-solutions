class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        letters = []

        for word in words:
            val = 0
            for c in word:
                val += weights[ord(c) - 97]

            letters.append(chr(122 - (val % 26)))

        return "".join(letters)
