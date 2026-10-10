class Solution:
    def canJump(self, nums: list[int]) -> bool:
        cur=nums[0]
        i=1
        n=len(nums)

        while i<n:
            if cur==0:
                return False
            
            if cur>n-i+1:
                return True
            
            cur-=1
            cur=max(cur,nums[i])
            i+=1
        return True

        