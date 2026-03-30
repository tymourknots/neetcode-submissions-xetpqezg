class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            middle = (top + bottom) // 2
            if matrix[middle][0] > target:
                bottom = middle - 1
            elif matrix[middle][-1] < target:
                top = middle + 1
            else:
                break
        
        middle = (top + bottom) // 2
        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[middle][mid] == target:
                return True
            elif matrix[middle][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False