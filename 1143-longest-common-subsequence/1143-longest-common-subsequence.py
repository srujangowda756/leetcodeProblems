class Solution:
    def help(self,t1,t2,i,j,dp):
        if i==len(t1) or j==len(t2):
            return 0
        
        if (i,j) in dp:
            return dp[(i,j)]

        if t1[i]==t2[j]:
            dp[(i,j)]= 1+self.help(t1,t2,i+1,j+1,dp)
            return dp[(i,j)]

        skip_1= self.help(t1,t2,i+1,j,dp)
        skip_2= self.help(t1,t2,i,j+1,dp) 

        dp[(i,j)]=max(skip_1,skip_2)
        return dp[(i,j)]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.help(text1,text2,0,0,{})
        
        
        