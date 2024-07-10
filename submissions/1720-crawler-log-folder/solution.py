class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for operation in logs:
            if operation == "../":
                depth = depth - 1 if depth != 0 else 0
            elif operation == "./":
                pass
            else:
                depth += 1

        return depth
