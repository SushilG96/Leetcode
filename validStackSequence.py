class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pos = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[pos]:
                pos += 1
                stack.pop()
        return stack == []
