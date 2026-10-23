class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowelsSet = {"a", "e", "i", "o", "u"}

        return " ".join(
            (word if word[0].lower() in vowelsSet else word[1:] + word[0])
            + "m"
            + "a" * aCount
            for aCount, word in enumerate(sentence.split(), start=2)
        )
