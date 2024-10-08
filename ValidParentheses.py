'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

'''
class Solution:


    def eliminate(self, our_string):

        
        if len(our_string)%2 != 0:
            return False


        right_pars = ['{', '[', '(']
        closed_pars = ['{}', '[]', '()']

        left_part = our_string[:int(len(our_string)/2)]
        right_part = our_string[-int(len(our_string)/2):]


        while left_part != '' and right_part != '':

            if left_part[-1:] in right_pars and left_part[-1:] + right_part[:1] in closed_pars:
                #Ordinary case () ({}) etc 

                left_part = left_part[:-1]
                right_part = right_part[1:]

            elif left_part[-1:] in right_pars:
                # case when {) 

                return False

            

            else:
                #case when (){}
                if self.eliminate(left_part) and self.eliminate(right_part):
                    left_part = ''
                    right_part = ''
                else:
                    return False
        
        return True







    def replacer(self, stringi):
        stringi = stringi.replace('{}','')
        stringi = stringi.replace('()','')
        stringi = stringi.replace('[]','')
        return stringi


    def isValid(self,  s: str):



        while s!='':
            replacer = self.replacer(s)
            if s == replacer:
                print('f')
                return False
            else:
                s = replacer

        print('t')
        return True





        
        #if self.eliminate(s): 
          # return True 


'''
        right_pars = ['1', '2', '3']
        left_pars = ['9', '4', '0']

        closed_parses = [10,6,3]
        
        our_string = s
        our_string = our_string.replace('{', '1')

        our_string = our_string.replace('[', '2')
        our_string = our_string.replace('(', '3')

        our_string = our_string.replace('}', '9')
        our_string = our_string.replace(']', '4')
        our_string = our_string.replace(')', '0')
'''


sol = Solution() 

sol.isValid("(([]){})") #{[]}{}([])"(([]){})"
