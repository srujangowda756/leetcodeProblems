class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        required_stack = {}
        for c in t:
            required_stack[c] = required_stack.get(c, 0) + 1

        window_counts = {}
        have, need = 0, len(required_stack)
        left = 0
        ans = ""
        ans_len = float("inf")

        for right in range(len(s)):
            c = s[right]
            if c in required_stack:
                window_counts[c] = window_counts.get(c, 0) + 1
                if window_counts[c] == required_stack[c]:
                    have += 1

            while have == need:
                if (right - left + 1) < ans_len:
                    ans = s[left:right + 1]
                    ans_len = right - left + 1

                left_char = s[left]
                if left_char in required_stack:
                    window_counts[left_char] -= 1
                    if window_counts[left_char] < required_stack[left_char]:
                        have -= 1
                left += 1

        return ans