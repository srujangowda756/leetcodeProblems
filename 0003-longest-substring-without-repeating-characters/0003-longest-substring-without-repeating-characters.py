class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        stack=[]
        left=0

        for right in range(len(s)):
            while s[right] in stack:
                stack.pop(0)
                left+=1   
            stack.append(s[right])
            ans=max(ans,right-left+1)
        return ans



        