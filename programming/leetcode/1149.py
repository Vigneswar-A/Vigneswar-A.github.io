class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        for i in arr1:
            if i in arr2 and i in arr3:
                yield i
                
        
        