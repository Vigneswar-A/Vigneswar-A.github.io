class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count=0
        for i in range(n:=len(nums)):
            for j in range(n):
                if i==j:
                    continue
                if nums[i]+nums[j]==target:
                    count+=1
        return count
        