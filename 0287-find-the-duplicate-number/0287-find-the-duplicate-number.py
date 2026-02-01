class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        seen=set()
        #for i in range(len(nums)):
            #if nums[i] in nums[i+1:]:
                #return nums[i]
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            seen.add(nums[i])