class Solution:
    def validateStackSequences(
        self, pushed: list[int], popped: list[int]
    ) -> bool:
        stack = []

        while pushed and popped:
            while popped and (not stack or stack[-1] != pushed[-1]):
                stack.append(popped.pop())
            while stack and pushed and stack[-1] == pushed[-1]:
                stack.pop()
                pushed.pop()

        return not (pushed or popped)
