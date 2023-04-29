class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return "\n".join(str(student) for student in self.students)
