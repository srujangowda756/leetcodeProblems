from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        required=Counter(s1)
        for i in range(len(s2)-n+1):
            if required==Counter(s2[i:i+n]):
                return True
                print(s2[i:i+n])
        return False