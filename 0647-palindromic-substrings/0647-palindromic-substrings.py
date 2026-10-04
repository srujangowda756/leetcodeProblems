class Solution:
    def help(self, s, l, r, dp):
        if l > r:
            return 0

        if dp[l][r] != -1:
            return dp[l][r]

        if s[l] == s[r]:
            if r - l <= 1 or self.help(s, l + 1, r - 1, dp):
                dp[l][r] = 1
                return 1

        dp[l][r] = 0
        return 0

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        ans = 0

        for l in range(n):
            for r in range(l, n):
                ans += self.help(s, l, r, dp)

        return ans