'''Given an array nums of distinct integers, return all the possible 
permutations
. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
'''
import random
import math
class Solution:
    # def factorial(self, n):
        
    #    factorial = 1
    #    while n > 1:
    #        factorial *= n
    #        n -= 1
    #    return factorial

    def permute(self, nums):
        number_of_combinations = math.factorial(len(nums))
        list_of_perms = []
        len_of_list = 0
        while len_of_list != number_of_combinations:
            random.shuffle(nums)
            if nums not in list_of_perms:
                adder = nums[:]
                list_of_perms.append(adder)
                len_of_list +=1
        print(list_of_perms)
        return list_of_perms



sol = Solution()
sol.permute([1,2,3])

