class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        ans = 0

        # Iterate over nums1 and find insertion position to nums2.
        nums2.reverse()
        for i in range(m):
            k = bisect.bisect_left(nums2, nums1[i])
            ans = max(ans, n - k - 1 - i)
        return ans
            
        