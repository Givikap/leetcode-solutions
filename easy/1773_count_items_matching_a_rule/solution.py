class Solution:
    def countMatches(
        self, items: list[list[str]], ruleKey: str, ruleValue: str
    ) -> int:
        idx = ("type", "color", "name").index(ruleKey)

        count = 0

        for item in items:
            if item[idx] == ruleValue:
                count += 1

        return count
