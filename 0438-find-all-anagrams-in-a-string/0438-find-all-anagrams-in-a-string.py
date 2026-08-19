class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        n=len(p)
        need={}
        have={}
        s_len=len(s)

        for i in range(97,97+26):
            need[chr(i)]=0
            have[chr(i)]=0
        for x in range(n):
            need[p[x]]+=1
            have[s[x]]+=1
        ans=[]
        for ch in range(n-1,len(s)):
            if have==need:
                ans.append(ch-n+1)
            have[s[ch-n+1]]-=1
            if ch+1<s_len:
                have[s[ch+1]]+=1
        return ans