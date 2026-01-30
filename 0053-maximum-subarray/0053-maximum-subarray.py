class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=float('-inf')
        for i in range(len(nums)):
            cursum=0
            for j in range(i,len(nums)):
                cursum+=nums[j]
                maxsum=max(maxsum,cursum)
        return maxsum