class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0 
        r = len(nums)-1
        num = nums[r]
        res = min(nums[l],nums[r])

        if nums[l] <= nums[r] : 
            return nums[l]
        


        while l <= r : 

            mid = (r - l)//2 + l 

            if nums[mid] > num : 
                l = mid + 1 
            
            elif nums[mid] <= num : 
                r = mid - 1 
                
            res = min(res,nums[mid])

        return res 

            

        