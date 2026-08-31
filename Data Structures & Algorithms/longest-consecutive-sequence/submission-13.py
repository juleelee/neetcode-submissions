class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == [] : 
            return 0 

        sorted_list = sorted(list(set(nums)))
        max = 1
        i = 0 
        local =1

        
        while i < len(sorted_list)-1: 
            
            
 
            if (sorted_list[i+1] == sorted_list[i] + 1) : 
                local +=1
                

                if local >= max : 
                    max = local 

            else : 
                local = 1 

            
            i = i+1 
        

        return max





        