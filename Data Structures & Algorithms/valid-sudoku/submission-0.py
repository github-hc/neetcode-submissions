class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Store numbers seen in each row
        rows = defaultdict(set)

        # Store numbers seen in each column
        cols = defaultdict(set)

        # Store numbers seen in each 3x3 box
        boxes = defaultdict(set)

        # Traverse every cell
        for r in range(9):
            for c in range(9):

                # Ignore empty cells
                if board[r][c] == ".":
                    continue

                num = board[r][c]

                # Identify which 3x3 box this cell belongs to
                box = (r // 3, c // 3)

                # Duplicate found
                if (
                    num in rows[r] or
                    num in cols[c] or
                    num in boxes[box]
                ):
                    return False

                # Remember this number
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

        return True