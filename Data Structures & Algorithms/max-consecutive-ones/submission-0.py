class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

            
        max = 0
        local = 0 
    

        for i in nums:
            if i == 1 :
                local+=1

            else :
                local = 0 

            if local > max :
                max = local 
        
        return max



            











        