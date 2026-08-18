class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        n=len(p)
        need=sorted(p)
        ans=[]
        for i in range(len(s)-n+1):
            if sorted(s[i:i+n])==need:
                ans.append(i)
        return ans



        