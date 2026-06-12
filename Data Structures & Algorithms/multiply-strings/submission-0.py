class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total_value = 0
        for i in range(len(num1)-1, -1, -1):
            left = int(num1[i]) * 10 ** (len(num1) - 1 - i)
            print(left)
            product = 0
            for j in range(len(num2)-1, -1, -1):
                right = int(num2[j]) * 10 ** (len(num2) - 1 - j)
                product += left * right
            total_value += product
        return str(total_value)