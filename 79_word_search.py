class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for x, row in enumerate(board):
            for y, char in enumerate(row):
                if char == word[0]: # foud first character of word!
                    if self.DFS(x, y, {(x,y)}, board, word): return True
        return False


    def DFS(self, x, y, visited_squares, board, word):
        next_char = len(visited_squares)

        if next_char >= len(word): return True

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_x, next_y = x + dx, y + dy
            next_square = (next_x, next_y)

            if (
                self.square_exists(next_x, next_y, board) and
                board[next_x][next_y] == word[next_char] and
                next_square not in visited_squares
            ):
                visited_squares.add(next_square)
                if self.DFS(next_x, next_y, visited_squares, board, word): return True

                # since visited_squares is passed by reference, pop the square from the set explicitly
                visited_squares.remove((next_x, next_y)) 

        return False


    def square_exists(self, x, y, board):
        return 0 <= x and x < len(board) and 0 <= y and y < len(board[0])

