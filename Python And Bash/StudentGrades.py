class StudentGrades:
    def __init__(self):
        self.grades = {}

    def add_student(self, name, grade):
        if name in self.grades:
            print(f"{name} already exists. Use update_grade to change the grade.")
        else:
            self.grades[name] = grade
            print(f"Added {name} with grade {grade}.")

    def update_grade(self, name, grade):
        if name in self.grades:
            self.grades[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print(f"{name} does not exist. Use add_student to add them first.")

    def print_grades(self):
        if not self.grades:
            print("No students found.")
        else:
            for name, grade in self.grades.items():
                print(f"{name}: {grade}")


# Example usage
if __name__ == "__main__":
    sg = StudentGrades()
    sg.add_student("Alice", 90)
    sg.add_student("Bob", 85)
    sg.update_grade("Alice", 95)
    sg.print_grades()