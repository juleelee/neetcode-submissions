import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        res = False 

        
        
        if len(s1) > len(s2) : 
            return res 

        dict_s1 = defaultdict(int, {letter: 0 for letter in string.ascii_lowercase})
        subdict = defaultdict(int, {letter: 0 for letter in string.ascii_lowercase})
        for i in range(len(s1)) :
            dict_s1[s1[i]] +=1 
            subdict[s2[i]] +=1 

        if subdict == dict_s1 : 
            return True

       

        l = 0
        for r in range(len(s1),len(s2)) : 

            subdict[s2[l]] -=1 

            subdict[s2[r]] +=1 
            
            if subdict == dict_s1 : 
                return True
            
            l +=1

            
        
        
        return res 

        