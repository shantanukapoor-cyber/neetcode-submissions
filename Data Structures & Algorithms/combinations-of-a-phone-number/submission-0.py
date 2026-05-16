class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits == "":
            return result
        mapping = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        def all_possible_strings(index, path):
            if index == len(digits):
                result.append(''.join(path))
                return
            possible_values = mapping[digits[index]]
            for letter in possible_values:
                path.append(letter)
                all_possible_strings(index + 1, path)
                path.pop()
        all_possible_strings(0, [])
        return result