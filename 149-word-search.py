from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, (i, j), word, 0, set()):
                        return True

        return False

    def dfs(self, board, starting_point, word, word_index, seen):
        r, c = starting_point
        if board[r][c] != word[word_index]:
            return False

        seen.add(starting_point)
        word_index += 1

        # In the following example,
        # [["a","b"],
        # ["c","d"]]
        # "acdb"
        # When we visit the last node, 'b', we don't have anything else to visit as
        # either we already saw the nodes, or they are out of range.
        # If we already found the string, we just stop.
        # An alternative would be to check for valid boundaries at the beginning of the function,
        # right after the word_index check.

        if word_index >= len(word):
            return True

        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nr = r + dy
            nc = c + dx

            if (0 <= nr < len(board) and 0 <= nc < len(board[0])) and (nr, nc) not in seen:
                if self.dfs(board, (nr, nc), word, word_index, seen):
                    return True

        # Backtrack: we are trying all possible path. After trying all four directions,
        # we remove the point from seen to make it available for future explorations.
        seen.remove(starting_point)

        return False


print(Solution().exist([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
print(Solution().exist([["a"]], "a"))
print(Solution().exist([["a", "b"], ["c", "d"]], "acdb"))
print(Solution().exist([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
