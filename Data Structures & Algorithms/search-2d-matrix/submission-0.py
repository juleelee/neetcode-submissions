class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

       
        line_top = 0

        line_down = len(matrix) - 1 

        n = len(matrix[0])

        line = -1 
        
        while line_top <= line_down : 

            line_mid = (line_down - line_top)//2 + line_top

            if matrix[line_mid][0] > target : 

                line_down = line_mid - 1 

            elif matrix[line_mid][n-1] < target : 
                line_top = line_mid + 1 
            
            else : 
                line = line_mid
                break


     
        if line == -1 : 
            return False 


        else : 

            nums = matrix[line]

            l = 0 
            r = n - 1 

            while l <= r : 
                mid = (r - l)//2 + l 

                if nums[mid] > target : 
                    r = mid - 1 
                elif nums[mid] < target : 
                    l = mid + 1 

                else :  
                    return True 
            
            return False 

                

