class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1 
        pivot = 0 
        while l < r : 
            mid = (r -l)//2 + l 

            if nums[mid] > nums[r] : 
                l = mid + 1 
            else : 
                r = mid

        pivot = l 
        print(pivot)
        l = 0 
        r = len(nums) - 1 

        if nums[pivot] <= target and target <= nums[r] : 
            l = pivot 
        else : 
            r = pivot - 1

        print(l,r)
        while l <= r : 

            mid = (r -l)//2 +l

            if nums[mid] > target : 
                r = mid - 1 
            elif nums[mid] < target : 
                l = mid + 1 
            else : 
                return mid
            
        return -1 
                
