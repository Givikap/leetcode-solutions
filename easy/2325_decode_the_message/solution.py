class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        chars = list(dict.fromkeys(c for c in key if c != " "))
        charsMap = {c: chr(97 + i) for i, c in enumerate(chars)}

        return "".join(charsMap.get(c, c) for c in message)
