class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morseMap = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        return len(
            set("".join(morseMap[ord(c) - 97] for c in word) for word in words)
        )
