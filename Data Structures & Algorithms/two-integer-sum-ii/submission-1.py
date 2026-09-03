class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind_left = 0
        ind_right = len(numbers) - 1
        left = numbers[ind_left]
        right = numbers[ind_right]
        
       
        sum = left + right

        while sum != target : 
            if sum > target :
                ind_right -=1
                right = numbers[ind_right]



            
            else : 
                ind_left +=1
                left = numbers[ind_left]

            sum = left + right







        return [ind_left+1,ind_right+1]



        