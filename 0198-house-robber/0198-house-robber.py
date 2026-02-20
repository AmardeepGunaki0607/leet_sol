class Solution:
    def rob(self, nums: List[int]) -> int:
    #     dp=[-1]*len(nums)
    #     return self.rec(0,nums,dp)

    # def rec(self,i,nums,dp):
    #     if i>=len(nums):
    #         return 0
    #     if dp[i]!=-1:
    #         return dp[i]
    #     take=nums[i]+self.rec(i+2,nums,dp)
    #     not_take=self.rec(i+1,nums,dp) 
    #     dp[i]=max(take,not_take)
    #     return dp[i]
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        return dp[-1]