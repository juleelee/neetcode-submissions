class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        


        sorted_list = sorted(nums)

        res = []


        for i in range(len(sorted_list)) : 
            l = i + 1 
            r = len(sorted_list) - 1 
            num = sorted_list[i]
            while l < r : 
                somme = num + sorted_list[l] + sorted_list[r] 

                if somme == 0 : 
                    
                    res.append([num, sorted_list[l],sorted_list[r]])
                    l +=1 
                
                elif somme > 0 : 

                    r -= 1 

                else : 

                    l += 1 

        

        res_final = []

        local_set = set()

        for l in res : 
            if tuple(l) not in local_set : 
                local_set.add(tuple(l))
                res_final.append(l)
        
        return res_final



