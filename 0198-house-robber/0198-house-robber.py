class Solution:
    def help(self,arr,n,dp):
        if n==0:
            return arr[n]
        if n==1:
            return max(arr[0],arr[1])
        if dp[n]!=-1:
            return dp[n]
        steel=self.help(arr,n-2,dp)+arr[n]
        not_steel=self.help(arr,n-1,dp)
        dp[n]= max(steel,not_steel)
        return dp[n]
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        track=[-1]*(n)
        return self.help(nums,n-1,track)

        