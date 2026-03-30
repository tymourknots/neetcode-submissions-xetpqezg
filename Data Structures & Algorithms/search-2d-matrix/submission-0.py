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
                left = 0
                right = len(matrix[0]) - 1

                while left <= right:
                    mid = (right + left) // 2
                    if matrix[middle][mid] == target:
                        return True
                    elif matrix[middle][mid] < target:
                        left = mid + 1
                    elif matrix[middle][mid] > target:
                        right = mid - 1
                return False
        return False


# matrix = [[1,2,4,8],    # -> matrix[0]
#         [10,11,12,13],  # -> matrix[1]
#         [14,20,30,40]]  # -> matrix[2] aka matrix[m - 1] aka matrix[len(matrix - 1)]
# target = 10
