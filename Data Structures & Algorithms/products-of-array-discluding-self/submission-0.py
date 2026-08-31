class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        zero = []
        total = 1

        for i in range(len(nums)) : 

            if nums[i] == 0 : 
                zero.append(i)
            else : 
                total = total*nums[i]

        res = [0]*len(nums)
        if len(zero) > 1 : 
            return res

        elif len(zero) == 1 :
            res[zero[0]] = total
            return res
        else : 
            for i in range(len(nums)):
                res[i] = int(total/nums[i])
            
            return res



        