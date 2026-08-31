class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        A = []

        for i, num in enumerate(nums,0): 
            A.append([num,i])

        A = sorted(A)


        i = 0
        j = len(nums)-1

        

        
        while i < j : 

            left_ind = A[i][1]
            right_ind = A[j][1]

            cur = nums[left_ind] + nums[right_ind]

            if cur == target :
                return [min(A[i][1], A[j][1]), max(A[i][1],A[j][1])]
            elif cur > target : 
                j -=1
            else : 
                i +=1

        return []



              










        