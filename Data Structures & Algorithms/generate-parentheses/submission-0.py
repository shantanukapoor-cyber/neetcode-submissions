class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # {( : n, ) : n}
        # subject to a constraint ( always before )
        # so we can select 1 to n open brackets first.
        # and then we can close brackets for 1 to i.
        # then we send this n-i as remainder so now we can place only n-i
        # okay. and then once remainder is 0 we push.
        result = []
        def print_result(opening, closing, answer):
            if opening == 0 and closing == 0:
                result.append("".join(answer))
                return
            if opening > 0:
                answer.append("(")
                print_result(opening-1, closing, answer)
                answer.pop()
            if closing > opening:
                answer.append(")")
                print_result(opening, closing-1, answer)
                answer.pop()
        print_result(n, n, [])
        return result
                
