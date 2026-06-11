class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        answer = []
        n = len(digits)
        for i in range(n-1, -1, -1):
            if i == n-1:
                digits[i] += 1
            new_value = digits[i] + carry
            carry = new_value // 10
            answer.append(new_value % 10)
        if carry != 0:
            answer.append(carry)
        return answer[::-1]