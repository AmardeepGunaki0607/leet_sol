class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=nums[0]
        c=1
        for i in range(1,len(nums)):
            if maj==nums[i]:
                c+=1
            else:
                c-=1
                if c==0:
                    maj=nums[i]
                    c=1
        return maj

        