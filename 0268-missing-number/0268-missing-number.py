class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #nums=list[]
        n=len(nums)
        for i in range(0,n+1):
            if i not in nums:
                return i
        
        