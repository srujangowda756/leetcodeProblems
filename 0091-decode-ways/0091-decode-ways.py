class Solution:
    def help(self,s,i,dp):
        if i==len(s):
            return 1

        if s[i]=='0':
            return 0
        
        if i in dp:
            return dp[i]

        ans = self.help(s, i + 1,dp)

        if i + 1 < len(s) and int(s[i:i+2]) <= 26:
            ans += self.help(s, i + 2,dp)

        dp[i]=ans
        return ans

    def numDecodings(self, s: str) -> int:
        return self.help(s,0,{})
        