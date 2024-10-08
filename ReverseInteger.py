'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

'''
class Solution:
    def reverse(self, x):
        window = range(-2**31, 2**31-1)
        if x<0: 
            negative = True
            x = str(x)[1:]
        else: 
            negative = False
            x = str(x)
        new_string_int = ''
        for i in range(1, len(x)+1):
            new_string_int += x[-i]
        
        if negative:new_int = -int(new_string_int)
        else: new_int = int(new_string_int)
        
        print(new_int)
        
        if new_int in window: return new_int
        else: return 0


            
        

sol = Solution()
sol.reverse(120)
        
