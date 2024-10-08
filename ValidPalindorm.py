'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.'''

class Solution:
    def string_handler(self, s):
        s = s.lower()
        symbols = [':',',','.','(',')',';',' ', '@', '{', '}', '[', ']', '+', '-', '#', '_', '"', '\'', '/', '\\']

        for symb in symbols:
            s = s.replace(symb, '')
        print(s)
        return s

        
    def isPalindrome(self, s):
        s = self.string_handler(s)
        stringa = [letter for letter in s]
        backwards = stringa[:]
        backwards.reverse()
        for i in range(0, len(stringa)):
            if stringa[i] == backwards[i]:
                pass
            else:
                print('false')
                return False
        print('true')
        return True


sol = Solution()
sol.isPalindrome(' ')
