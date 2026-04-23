class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # push in stack.
        # when operator get,
        # pop twice, apply op, push result.
        # continue till end.
        op = set(['+','-','*','/'])
        stack = []
        for token in tokens:
            if token not in op:
                stack.append(token)
            else:
                rhs = int(stack.pop())
                lhs = int(stack.pop())
                if token == '+':
                    result = lhs + rhs
                    stack.append(result)
                elif token == '-':
                    result = lhs - rhs
                    stack.append(result)
                elif token == '*':
                    result = lhs * rhs
                    stack.append(result)
                elif token == '/':
                    result = lhs / rhs
                    stack.append(result)
        return int(stack.pop())
