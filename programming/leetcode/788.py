class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        
        
        def ispossible(target):
            count = k
            for i in range(len(stations)-1):
                count -= (stations[i+1]-stations[i])//target
                if count < 0:
                    return False
            return True
        
        left = 0
        right = max(stations)
        acc = 10**-6
        
        while left <= right:
            mid = (left+right)/2
            if ispossible(mid):
                right = mid-acc
            else:
                left = mid+acc
                
        return left
                
        
        
                    
                