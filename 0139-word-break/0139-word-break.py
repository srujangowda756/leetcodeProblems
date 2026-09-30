class Solution:
    def helps(self, s, words, i, dp):
        if i == len(s):
            return True

        if i in dp:
            return dp[i]

        for word in words:
            if s.startswith(word, i):
                if self.helps(s, words, i + len(word), dp):
                    dp[i] = True
                    return True

        dp[i] = False
        return False

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        return self.helps(s, wordDict, 0, {})