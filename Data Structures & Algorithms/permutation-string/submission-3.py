class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        res = False 

        
        
        if len(s1) > len(s2) : 
            return res 

        dict_s1 = defaultdict(int)

        for c in s1 : 
            dict_s1[c] +=1 

        l = 0 
        r = len(s1)

       
        while r < len(s2)+1 : 
            subdict = defaultdict(int)
            for i in range(l,r) : 
                subdict[s2[i]] +=1 
            if subdict == dict_s1 : 
                return True

            
            l +=1
            r +=1

        
        return res 

        