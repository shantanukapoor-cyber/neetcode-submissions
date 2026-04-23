class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fullproduct = 1
        zerocount = 0
        for num in nums:
            if num == 0:
                zerocount += 1
                if zerocount > 1:
                    return [0]*len(nums)
            fullproduct = fullproduct * num
        answer = []
        if zerocount != 0:
            zeroindex = -1
            product = 1
            for i in range(len(nums)):
                if nums[i] == 0:
                    zeroindex = i
                else:
                    product = product * nums[i]
            for i in range(len(nums)):
                if i == zeroindex:
                    answer.append(product)
                else:
                    answer.append(0)
            return answer

        for num in nums:
            answer.append(fullproduct//num)
        return answer