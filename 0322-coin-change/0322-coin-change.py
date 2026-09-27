class Solution:
    def help(self,arr,k,curr,dp):
        if curr==k:
            return 0
        if curr>k:
            return float("inf")
        if curr in dp:
            return dp[curr]
        temp=float("inf")
        for i in arr:
            temp=min(temp,self.help(arr,k,curr+i,dp)+1)
        dp[curr]=temp
        return dp[curr]
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp={}
        ans = self.help(coins, amount,0,dp)
        if ans == float("inf"):
            return -1

        return ans