class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                return nums[i]
                
        