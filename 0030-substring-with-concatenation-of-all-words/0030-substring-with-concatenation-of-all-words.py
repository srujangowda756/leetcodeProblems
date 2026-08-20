from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k=len(words[0])
        total_len=len(words)*k
        word_count=Counter(words)
        result=[]          

        for i in range(len(s)-total_len+1):
            window=s[i:i+total_len]
            
            chunks=[]
            for j in range(0,len(window),k):
                chunks.append(window[j:j+k])
            if Counter(chunks)==word_count:
                result.append(i)                
        return result

                

        