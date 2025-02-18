from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 9 sub-boxes

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)  # Compute box index
                print(box_index)
                if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

        return True
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]