class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for i in range(len(operations)):
            operation = operations[i]

            if operation == '+':
                scores.append(scores[-1] + scores[-2])

            elif operation == 'D':
                scores.append(scores[-1] * 2)

            elif operation == 'C':
                scores.pop()

            else:
                scores.append(int(operation))
        
        return sum(scores)