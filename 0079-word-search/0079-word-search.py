class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        if len(word) > m * n:
            return False

        from collections import Counter

        board_count = Counter(c for row in board for c in row)
        word_count = Counter(word)

        for c, count in word_count.items():
            if board_count[c] < count:
                return False

        if board_count[word[-1]] < board_count[word[0]]:
            word = word[::-1]

        def dfs(i, j, k):
            if k == len(word):
                return True

            if (i < 0 or j < 0 or i >= m or j >= n
                    or board[i][j] != word[k]):
                return False

            temp = board[i][j]
            board[i][j] = "#"

            found = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            )

            board[i][j] = temp
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False