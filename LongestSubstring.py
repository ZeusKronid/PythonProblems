'''Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        if s == '':
            return 0 

        appender = ''
        
        stringers = []

        while s != '':
            for i in s:
                if i not in appender: 
                    appender +=i
                else:
                    stringers.append(appender)
                    s = s[1:]
                    appender = ''
                    break

        maxer = max(map(lambda x: len(x), stringers))
        print(maxer)
        return maxer



sol = Solution()
sol.lengthOfLongestSubstring("dvdf")

