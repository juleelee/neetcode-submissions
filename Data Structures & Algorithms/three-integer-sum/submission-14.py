class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        


        sorted_list = sorted(nums)

        res = []


        for i in range(len(sorted_list)) : 

            if sorted_list[i] > 0 :
                break 

            if i > 0 and sorted_list[i] == sorted_list[i-1] : 
                continue 


            l = i + 1 
            r = len(sorted_list) - 1 
            num = sorted_list[i]
            while l < r : 
                somme = num + sorted_list[l] + sorted_list[r] 

                if somme == 0 : 
                    
                    res.append([num, sorted_list[l],sorted_list[r]])
                    l +=1 
                    r -=1 
                    while l < r and sorted_list[l] == sorted_list[l-1] : 
                        l +=1 

                
                elif somme > 0 : 

                    r -= 1 

                else : 

                    l += 1 

        

        
        return res



