class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        chosenRow = None
        while l <= r:
            mid = (r + l) // 2
            if target < matrix[mid][0]:
                r = mid -1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                break
        
        chosenRow = (l+r) // 2
        l, r = 0, len(matrix[chosenRow])-1
        while l <= r:
            mid = l + (r - l) // 2
            if target < matrix[chosenRow][mid]:
                r = mid -1
            elif target > matrix[chosenRow][mid]:
                l = mid + 1
            else:
                return True
        
        return False