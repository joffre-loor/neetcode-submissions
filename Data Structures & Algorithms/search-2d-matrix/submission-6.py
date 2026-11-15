class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        rowL, rowR = 0, len(matrix)-1

        while rowL <= rowR:
            midRow = rowL + ((rowR-rowL) // 2)
            print(f"{midRow}, {rowL}, {rowR}")
            if matrix[midRow][0] >= target or target <= matrix[midRow][-1]:
                print("here")
                colL, colR = 0, len(matrix[0])-1
                while colL <= colR:
                    midCol = colL + ((colR-colL) // 2)

                    if matrix[midRow][midCol] == target:
                        return True
                    
                    if matrix[midRow][midCol] < target:
                        colL = midCol+1
                    else:
                        colR = midCol-1
            
            if matrix[midRow][0] > target:
                rowR = midRow-1
            else:
                rowL = midRow+1

        return False

