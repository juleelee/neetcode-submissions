class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        left_ind = 0 
        right_ind = len(nums) - 1 
        
        res = []

        sorted_nums = sorted(nums)


        
        for i in range(len(nums)-1) : 

            
            num = sorted_nums[i]

            left_ind = i+1
            right_ind = len(nums) - 1 

            left =  sorted_nums[left_ind]
            right = sorted_nums[right_ind]

            while left_ind < right_ind : 

            
                sum_local = left + right + num
                
                if sum_local == 0 : 
                    res.append([left,num,right])
                    right_ind -= 1
                    right = sorted_nums[right_ind]

                elif sum_local > 0 : 
                    right_ind -= 1
                    right = sorted_nums[right_ind]
                else : 
                    left_ind +=1
                    left =  sorted_nums[left_ind]

                

                    







            
        seen = set()
        res_final = []
        for sublist in res : 
            tuple_list = tuple(sublist)
            if tuple_list not in seen : 
                seen.add(tuple_list)
                res_final.append(sublist)
            

        return res_final
            


            






