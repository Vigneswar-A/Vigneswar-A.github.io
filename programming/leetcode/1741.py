class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(nums,key=lambda n:(nums.count(n),-n))