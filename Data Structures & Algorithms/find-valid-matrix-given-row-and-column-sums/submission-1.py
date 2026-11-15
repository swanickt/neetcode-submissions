class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0] * len(colSum) for _ in range(len(rowSum))]

        for i in range(len(rowSum)): 
            matrix[i][0] = rowSum[i]
        
        for j in range(len(colSum)-1):
            i = 0
            col_value = sum(matrix[k][j] for k in range(len(rowSum)))
            while col_value > colSum[j]:
                
                value_to_move = min(matrix[i][j], col_value - colSum[j])
                matrix[i][j+1] += value_to_move
                matrix[i][j] -= value_to_move
                col_value -= value_to_move

                i += 1

        return matrix