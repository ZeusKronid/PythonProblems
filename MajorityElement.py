'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums):
        set_of_elements = set(nums)
        list_of_elements = []
        list_of_freqs = []
        for element in set_of_elements:
            list_of_elements.append(element)
            list_of_freqs.append(nums.count(element))
        
        index_of_highest_element = list_of_freqs.index(max(list_of_freqs))
        number_found = list_of_elements[index_of_highest_element]
        print(number_found)
        return number_found
        


sol = Solution()
sol.majorityElement([2,2,1,1,1,2,2])

