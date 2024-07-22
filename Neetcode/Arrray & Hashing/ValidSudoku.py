'''https://neetcode.io/problems/valid-sudoku'''
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Check duplicates
        # On rows
        for i in range(9):
            s = set(board[i])
            s.remove(".")
            if len(s) != len([num for num in board[i] if num != "."]):
                return False
        # On cols
        for j in range(9):
            s = set()
            l = []
            for i in range(9):
                if board[i][j] != ".":
                    s.add(board[i][j])
                    l.append(board[i][j])
            if len(s) != len(l):
                return False
        # In sub-boxes
        centers = [(1, 1),(1, 4),(1, 7),(4, 1),(4, 4),(4, 7),(7, 1),(7, 4),(7, 7)]
        offsets = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 0),(0, 1),(1, -1),(1, 0),(1, 1)]
        for center in centers:
            s = set()
            l = []
            x = center[0]
            y = center[1]
            for offset in offsets:
                offsetX = offset[0]
                offsetY = offset[1]
                num = board[x + offsetX][y + offsetY]
                if num != ".":
                    s.add(num)
                    l.append(num)
            if len(s) != len(l):
                return False
        return True

# Same as neetcode.io's solution, but not using default dict
class Solution2:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = dict()
        cols = dict()
        boxes = dict() # key = (r / 3, r / 3)

        for r in range(9):
            for c in range(9):
                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if (r // 3, c // 3) not in boxes:
                    boxes[(r // 3, c // 3)] = set()
                if board[r][c] == ".":
                    continue
                if(
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in boxes[(r//3, c//3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        return True