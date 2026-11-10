import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # treat it as any other 2D list and binary search
        
        row_size = len(matrix[0])
        
        L = 0
        R = len(matrix) * row_size - 1

        while L <= R:

            m = (L + R) // 2

            row = m // row_size

            column = m % row_size

            if matrix[row][column] == target:
                return True
            
            elif matrix[row][column] < target:
                L = m + 1
            else:
                R = m - 1


        return False



        