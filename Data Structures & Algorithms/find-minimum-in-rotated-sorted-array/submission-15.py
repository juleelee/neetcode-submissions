class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0 
        r = len(nums)-1
   
        res = nums[0]

   
        


        while l <= r : 

            if nums[l] <= nums[r] : 
                return min(res, nums[l])

            mid = (r - l)//2 + l 

            if nums[mid] > nums[r] : 
                l = mid + 1 
            
            elif nums[mid] < nums[r] : 
                r = mid - 1 
                
            res = min(res,nums[mid])

        return res 

            

        