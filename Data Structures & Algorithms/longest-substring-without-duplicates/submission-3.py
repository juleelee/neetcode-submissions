class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        dict_local = set()
        res = 0


        for r in range(len(s)) : 

            while s[r] in dict_local : 
                dict_local.remove(s[l])
                l +=1 
            
            dict_local.add(s[r])
            res = max(res, r-l+1)
            

        return res



        