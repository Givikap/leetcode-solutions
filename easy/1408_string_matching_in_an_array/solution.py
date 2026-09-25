class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        substrings = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue

                if words[i] in words[j]:
                    substrings.append(words[i])
                    break

        return substrings
