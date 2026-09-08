class Solution:
    def maxArea(self, heights: List[int]) -> int:



        l = 0
        r = len(heights)-1

        
        area = 0 

        while l < r : 

            area_local = (r-l)*min(heights[l],heights[r])

            if area_local > area : 
                area = area_local 

            
            if heights[l] > heights[r] : 
                r -= 1 
            else : 
                l +=1 
        
        return area







        
        