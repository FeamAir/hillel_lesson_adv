class Student:
    """Class Student - student data"""

    def __init__(self, name, surname, grade):
        self.name = name
        self.surname = surname
        self.grade = grade

    def add_grade(self, grades):
        """Add new grade"""
        self.grade = grades
        return self.grade

    def display(self):
        """Display student"""
        print('Name: {}. Surename: {}. Grade: {}'.format(self.name,
                                                         self.surname,
                                                         self.grade))


class Group:
    """Class Group - create Group and save list students """

    journal = []

    def __init__(self, name):
        self.name = name
        self.journal = []

    def add_student(self, students: list):
        """Add students to the group"""
        new_student = Student(*students)
        self.journal.append(new_student)

    def display_group(self, ):
        """Display Group"""
        print("Group:", self.name)
        [Student.display(student) for student in self.journal]


if __name__ == "__main__":
    std = Student("Ivan", "Solmur", 4)
    std.display()
    std.add_grade(5)
    std.display()
    std1 = Group("2021")
    std1.add_student(["Urii", "Borkin", 5])
    std1.add_student(["vitalii", "Kolkis", 4])
    std1.display_group()
    std2 = Group("2022")
    std2.add_student(["Svetlana", "Rosta", 3])
    std2.add_student(["Irina", "Losk", 5])
    std2.display_group()
