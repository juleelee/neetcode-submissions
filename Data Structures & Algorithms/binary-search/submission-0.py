class Solution:
    def search(self, nums: List[int], target: int) -> int:

    

        l = 0 
        r = len(nums) - 1

        if nums[l] == target : 
            return l 
        
        if nums[r] == target : 
            return r 

        mid = (r - l)//2 + l 

        while l < r: 

            mid = (r - l)//2 + l 

            if mid == r or mid == l : 
                return -1 
            

            if nums[mid] == target : 
                return mid 

            elif nums[mid] > target:
                r = mid 
            elif nums[mid] < target:  
                l = mid 

        return -1 



            

        