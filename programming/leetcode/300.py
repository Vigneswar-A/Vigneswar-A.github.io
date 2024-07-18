class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        sub = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                j = bisect.bisect_left(sub, nums[i])
                sub[j] = nums[i]
        print(sub)
        return len(sub)
                