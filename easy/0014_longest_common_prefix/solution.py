class Solution:
    def longestCommonPrefix(self, words: list[str]) -> str:
        longest_common_prefix = words[0]

        for word in words[1:]:
            i = 0
            end = min(len(word), len(longest_common_prefix))

            while i < end and word[i] == longest_common_prefix[i]:
                i += 1

            if i == 0:
                return ""
            elif i < len(longest_common_prefix):
                longest_common_prefix = longest_common_prefix[:i]

        return longest_common_prefix
