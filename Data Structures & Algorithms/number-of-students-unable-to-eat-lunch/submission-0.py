class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # The key insight is that student order does not matter.
        # Since students can rotate indefinitely, what matters is 
        # whether there exists any student who wants the current top sandwich.

        remaining_students = len(students)
        counts = Counter(students)

        for sandwich in sandwiches:
            if counts[sandwich] > 0:
                remaining_students -= 1
                counts[sandwich] -=1
            else:
                break
        return remaining_students