class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        chars_counter = [0] * 26

        for c in chars:
            chars_counter[ord(c) - 97] += 1

        chars_count = 0

        for word in words:
            chars_counter_copy = chars_counter.copy()

            for c in word:
                c_i = ord(c) - 97

                if chars_counter_copy[c_i] == 0:
                    break

                chars_counter_copy[c_i] -= 1
            else:
                chars_count += len(word)

        return chars_count
