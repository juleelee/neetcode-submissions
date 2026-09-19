class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        sorted_piles = sorted(piles)

        m = sorted_piles[len(sorted_piles) - 1]

        l = 1 
        r = m
        res = m
        while l <= r : 

            mid = (r - l)//2 + l 

            sum = 0 
            for num in sorted_piles :  
                sum += -(-num// mid)
            

            if sum > h :    
                l = mid + 1 

            elif sum <= h: 
                r = mid - 1 

                res = min(res,mid)

            


                

        return res 