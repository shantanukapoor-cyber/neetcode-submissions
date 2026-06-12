class Solution:
    def getSum(self, a: int, b: int) -> int:
        # A bitmask of 32 ones. This forces Python to behave like a 32-bit computer, 
        # which prevents infinite loops when dealing with negative numbers.
        mask = 0xFFFFFFFF
        
        while b & mask != 0:
            # 1. Find where the carries happen, and shift them left by 1 column
            carry = (a & b) << 1
            
            # 2. Add the numbers together while ignoring the carries
            a = a ^ b
            
            # 3. Put the carries into 'b' so they get added in the next loop
            b = carry
            
        # If the number is positive, return it. If negative, format it correctly for Python.
        return (a & mask) if b > 0 else a