class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        charsMap = [""] * 26

        k = 0
        i = 0
        while k < len(key) and i < 26:
            c = ord(key[k]) - 97
            if key[k].isalpha() and charsMap[c] == "":
                charsMap[c] = chr(97 + i)
                i += 1

            k += 1

        return "".join(
            charsMap[ord(c) - 97] if c.isalpha() else " " for c in message
        )
