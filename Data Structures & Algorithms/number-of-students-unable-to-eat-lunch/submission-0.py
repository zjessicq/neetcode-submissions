class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        i = 0       # index of the sandwich currently on top
        skips = 0   # how many students in a row have refused the top sandwich

        while queue and skips < len(queue):
            if queue[0] == sandwiches[i]:
                queue.popleft()   # student takes it and leaves
                i += 1            # next sandwich is now on top
                skips = 0
            else:
                queue.append(queue.popleft())  # student goes to the back
                skips += 1

        return len(queue) 
        