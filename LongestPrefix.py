class Solution:
    def longestCommonPrefix(self, strs):
        prefix = []
        if len(strs) > 1:

            shortest_word = min(strs, key=len)
            strs.remove(shortest_word)

            words_as_chars = []
            for word in strs:
                words_as_chars.append([char for char in word])
            
            found_prefix = False
            for i in range(0, len(shortest_word)):

                for word in words_as_chars:
                    if word[i] == shortest_word[i]:
                        if word is words_as_chars[-1]:
                            prefix.append(word[i])
                    else: 
                        found_prefix=True
                        break

                if found_prefix: break 

            prefix = ''.join(prefix)

        else:
            prefix = strs[0]
            
        print(prefix)
        return prefix
         

sol = Solution()
sol.longestCommonPrefix(["flower","flow","flight"])
