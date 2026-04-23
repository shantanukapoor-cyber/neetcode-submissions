class Solution:
    def isValid(self, s: str) -> bool:
        # simple.
        # first should always be open bracket. if closed bracket then false.
        # when stack empty, can only be ( [ {.
        # push these tokens.
        # now next can either be another opening bracket or closing for the
        # top value.
        # if any other than false.
        # after everything it's true.
        stack = []
        mapping = {'(':')', '[':']', '{':'}'}
        for bracket in s:
            print(bracket, bracket in mapping, mapping)
            if len(stack) == 0:
                if bracket in mapping:
                    stack.append(bracket)
                else:
                    return False
            else:
                if mapping[stack[-1]] == bracket:
                    stack.pop()
                else:
                    if bracket in mapping:
                        stack.append(bracket)
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
        