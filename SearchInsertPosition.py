'''

Given a sorted array of distinct 
integers and a target value, return the index if the target is found. If not, 
return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

class Solution:
    def searchInsert(self, nums, target):
        try:
            index = nums.index(target)
            return index
        except ValueError:
            nums.append(target)
            nums.sort()
            index = nums.index(target)
            return index

sol = Solution()
sol.searchInsert([1,3,5,6],2)

