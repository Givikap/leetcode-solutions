class Solution:
    def combinationSum(
        self, candidates: list[int], target: int
    ) -> list[list[int]]:
        candidates.sort()

        combinations = []
        stack = [([], 0, 0)]

        while stack:
            curr_combination, curr_sum, index = stack.pop()

            if curr_sum == target:
                combinations.append(curr_combination)
                continue
            if curr_sum > target:
                continue

            for i in range(index, len(candidates)):
                if curr_sum + candidates[i] <= target:
                    stack.append(
                        (
                            curr_combination + [candidates[i]],
                            curr_sum + candidates[i],
                            i,
                        )
                    )

        return combinations
