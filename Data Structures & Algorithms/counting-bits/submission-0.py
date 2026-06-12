class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        M = 1
        while n > M:
            M = M * 2
        for i in range(n+1):
            temp = M
            count = 0
            while temp > 0:
                if i >= temp:
                    count += 1
                i = i % temp
                temp = temp // 2
            output.append(count)
        return output
