'''Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 '''


class Solution:
    
    def palindrom_checker(self, s):
        if len(s) == 1:
            return False 
        
        left_part = s[:int(len(s)/2)]

        if len(s)%2 != 0: 
            right_part = s[int(len(s)/2)+1:]
        else:
            right_part = s[int(len(s)/2):]
        
        if left_part == right_part[::-1]:
            return True
        else:
            return False 


    def longestPalindrome(self, s):
        myS = s
        string_checker = ''
        pal_arr = []
        while myS != '':
            for i in myS:
                string_checker += i
                if self.palindrom_checker(string_checker):
                    pal_arr.append(string_checker)

            string_checker = ''
            myS = myS[1:]
        if len(pal_arr)==0:
            print(s[0])
            return s[0]

        list_of_len = list(map(lambda x: len(x), pal_arr))
        longest_len = max(list_of_len)
        longest_pal = pal_arr[list_of_len.index(longest_len)]
        print(longest_pal)
        return longest_pal

            

sol = Solution()
sol.longestPalindrome('thelviymgkeddreyviespjsyqwmbmnlwzjhdokfzrczvreiagayofwvhecskjqlqzodtozvzozqyiwfsjyrinrmgfyhplybonzuvmxxyihmggwiuccplqjtgschmieoexvtewbsjqzkzapfxpzhgjtbmlchevohmxnbattphvobptnhmcoihcaimchurqpucxapojgszpopdvsfahwidiyxlpjfhdkcoewzvlmaebudtovnvcuadykhhmwfpilqfdvnseiitokcbuxmhwukrdxwvtgztczrwcsydqwosnktronibiplbljrcpinqorbhxrwjonnqeniebrksjkcmbvjnuwdedoenqmrcxayqbzmlpbubnfnkkqnuljtchaeijcmfpyuxkgfssoqliqmhowtbmcvzkqbanxhowjjejexxlihwwhilxxejejjwohxnabqkzvcmbtwohmqilqossfgkxuypfmcjieahctjlunqkknfnbubplmzbqyaxcrmqneodedwunjvbmckjskrbeineqnnojwrxhbroqnipcrjlblpibinortknsowqdyscwrzctzgtvwxdrkuwhmxubckotiiesnvdfqlipfwmhhkydaucvnvotdubeamlvzweockdhfjplxyidiwhafsvdpopzsgjopaxcupqruhcmiachiocmhntpbovhpttabnxmhovehclmbtjghzpxfpazkzqjsbwetvxeoeimhcsgtjqlpccuiwggmhiyxxmvuznobylphyfgmrniryjsfwiyqzozvzotdozqlqjkscehvwfoyagaiervzcrzfkodhjzwlnmbmwqysjpseivyerddekgmyivleht')
