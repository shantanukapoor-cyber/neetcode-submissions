class Solution:
    def reverse(self, x: int) -> int:
        # Define the strict 32-bit signed integer boundaries
        MIN_INT = -2**31      # -2147483648
        MAX_INT = 2**31 - 1   #  2147483647
        
        # 1. Isolate the sign so we can do clean decimal math on positive numbers
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        while x > 0:
            # 2. Extract the last digit
            digit = x % 10
            x //= 10
            
            # 3. Before multiplying by 10, check if it will breach the 32-bit limit.
            # In a strict environment, we divide the limit by 10 to check *before* the overflow occurs.
            if reversed_num > (MAX_INT - digit) // 10:
                return 0
                
            reversed_num = (reversed_num * 10) + digit
            
        # 4. Restore the sign to the final output
        final_result = sign * reversed_num
        
        return final_result
