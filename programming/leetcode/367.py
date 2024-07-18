class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left , right = 0 , ceil(num/2)
        
        while left <= right:
            mid = left + right >> 1
            square = mid*mid
            
            if square == num:
                return True
            
            elif square < num:
                left = mid + 1
                
            else:
                right = mid - 1
                
        return False
                
                
                
                
        
        
        