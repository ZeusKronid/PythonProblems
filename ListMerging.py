#Definition for singly-linked list.
class Solution:
    def mergeTwoLists(self, list1, list2):
        list_to_return=[]


        if list1[-1] > list2[-1]:
            list_with_larger_last_element = list1
            another_list = list2
        else: 
            list_with_larger_last_element = list2
            another_list = list1
        


        for element in list_with_larger_last_element:
            values = [x for x in another_list if x <= element]
            another_list = [x for x in another_list if x not in values]

            list_to_return.extend(values)

            list_to_return.append(element)
         
        print(list_to_return)
        return list_to_return

sol = Solution()
sol.mergeTwoLists([],[0])
