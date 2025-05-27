# Parent class
class Person:
    def __init__(self, name, age, university_id):
        self.name = name
        self.age = age
        self.university_id = university_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"University ID: {self.university_id}")

# Subclass: Student
class Student(Person):
    def __init__(self, name, age, university_id, course, year):
        super().__init__(name, age, university_id)
        self.course = course
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Role: Student")
        print(f"Course: {self.course}")
        print(f"Year: {self.year}")

# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, name, age, university_id, department, subjects):
        super().__init__(name, age, university_id)
        self.department = department
        self.subjects = subjects  # list of subjects taught

    def display_info(self):
        super().display_info()
        print(f"Role: Lecturer")
        print(f"Department: {self.department}")
        print(f"Subjects Taught: {', '.join(self.subjects)}")

# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, university_id, position, office):
        super().__init__(name, age, university_id)
        self.position = position
        self.office = office

    def display_info(self):
        super().display_info()
        print(f"Role: Staff")
        print(f"Position: {self.position}")
        print(f"Office: {self.office}")

# Examples
print("\n--- Student Info ---")
student = Student("Alice", 20, "U2025001", "Computer Science", 2)
student.display_info()

print("\n--- Lecturer Info ---")
lecturer = Lecturer("Dr. John", 45, "U1003002", "Engineering", ["Thermodynamics", "Fluid Mechanics"])
lecturer.display_info()

print("\n--- Staff Info ---")
staff = Staff("Mr. Henry", 38, "U3009005", "Admin Officer", "Main Block - Room 102")
staff.display_info()
