'''Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

[1,2,3,4]
[[],[1],[2],[3],[4],[1,2,3],[1,3,4] [1,2,3,4]]


[3,2,4,1]
[1,2,3,4]


[,[1,2,4]]
my 
,,,]

 '''


#ВСЮ ИДЕЮ НУЖНО ПЕРЕДЕЛАТЬ ОКНО НЕ ПОДХОДИТ Т.К ЕСТЬ 124 ОКНО РАССЫПАЕТСЯ НУЖНО ДЕЛАТЬ УБИВАНИЕ СПИСКА 
import math

class Solution:
    def subsets(self, nums):
        appender = [tuple([]), tuple(nums)]
        if len(nums) == 1: return [[],nums]
        for i in range(0, len(nums)):
            slide = len(nums)-2 
            little_appender = [nums[i]]
            appender.append(tuple([nums[i]]))
            while slide != 0:
                slide_window = (len(nums)-1-slide)+1
                for window in range(1, slide_window+1):
                    print(i, slide, slide_window, nums[i+window:i+window+slide_window-1])
                    little_appender.extend(nums[i+window:i+window+slide_window-1])
                    appender.append(tuple(little_appender))
                    little_appender = [nums[i]]
                slide = slide-1

        settik = {i for i in appender}
        appender = [list(i) for i in settik]
        for lst in appender:
            lst.sort()
        
                
        
        
                
        print(appender)
        return appender 

sol = Solution()
sol.subsets([3,2,4,1])
