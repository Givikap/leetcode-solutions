class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        for row in range(len(board)):
            for col in range(len(board[0])):
                live_neighbors_count = 0

                for row_offset in (-1, 0, 1):
                    for col_offset in (-1, 0, 1):
                        if row_offset == 0 and col_offset == 0:
                            continue

                        r, c = row + row_offset, col + col_offset

                        if 0 <= r < len(board) and 0 <= c < len(board[0]):
                            if board[r][c] == 1 or board[r][c] == 2:
                                live_neighbors_count += 1

                if board[row][col] == 1 and (
                    live_neighbors_count < 2 or live_neighbors_count > 3
                ):
                    board[row][col] = 2
                elif board[row][col] == 0 and live_neighbors_count == 3:
                    board[row][col] = -1

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == -1:
                    board[row][col] = 1
                elif board[row][col] == 2:
                    board[row][col] = 0
