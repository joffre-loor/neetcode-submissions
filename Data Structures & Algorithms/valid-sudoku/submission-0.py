class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = {}
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                col_quad = col // 3
                row_quad = row // 3
                quad = f"quad{row_quad}{col_quad}"
                if quad not in hashmap:
                    hashmap[quad] = set()
                if f"row{row}" not in hashmap:
                    hashmap[f"row{row}"] = set()
                if f"col{col}" not in hashmap:
                    hashmap[f"col{col}"] = set()
                row_set = hashmap[f"row{row}"]    
                col_set = hashmap[f"col{col}"]
                quad_set = hashmap[quad]
                if board[row][col] in row_set:
                    return False
                else:
                    row_set.add(board[row][col])
                
                if board[row][col] in col_set:
                    return False
                else:
                    col_set.add(board[row][col])
                
                if board[row][col] in quad_set:
                    return False
                else:
                    quad_set.add(board[row][col])
        return True