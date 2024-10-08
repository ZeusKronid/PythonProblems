'''Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.'''

class Solution:
    def thirdMax(self, nums):
        if len(nums) == 1: 
            print(nums[0])
            return nums
        elif len(nums) == 0:
            print([])
            return nums
        
        nums = list(set(nums))
        if len(nums) < 3:
            print(max(nums))
            return max(nums)
        for i in range(0,2):
            print(nums)
            nums.remove(max(nums))
        print(max(nums))
        return max(nums)

sol = Solution()
sol.thirdMax([1,2,2,5,3,5])


