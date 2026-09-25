class Solution:
    def vowelStrings(
        self, words: list[str], queries: list[list[int]]
    ) -> list[int]:
        vowels = "aeiou"

        prefixSums = [0] * (len(words) + 1)

        for i in range(1, len(words) + 1):
            prefixSums[i] = prefixSums[i - 1] + (
                words[i - 1][0] in vowels and words[i - 1][-1] in vowels
            )

        results = []

        for li, ri in queries:
            results.append(prefixSums[ri + 1] - prefixSums[li])

        return results
